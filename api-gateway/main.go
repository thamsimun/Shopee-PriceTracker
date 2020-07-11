package main

import (
	"context"
	"encoding/gob"
	"flag"
	"log"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"google.golang.org/grpc"

	"github.com/gin-contrib/cors"
	"github.com/gorilla/securecookie"
	"github.com/gorilla/sessions"
	"github.com/zsais/go-gin-prometheus"

	priceServicePackage "git.garena.com/simun.tham/entry-task/api-gateway/price-proto"
	userServicePackage "git.garena.com/simun.tham/entry-task/api-gateway/user-proto"
)

var (
	userServiceGrpcAddr  = flag.String("user_server_addr", "user-service:50051", "Address for outgoing requests to user service")
	priceServiceGrpcAddr = flag.String("price_server_addr", "price-service:8080", "Address for outgoing requests to price service")
	httpAddr             = flag.String("http_addr", ":8181", "Address for incoming http requests")
)

// var store = sessions.NewCookieStore([]byte(os.Getenv("SESSION_KEY")))

type LOGIN struct {
	USER     string `json:"user" binding:"required"`
	PASSWORD string `json:"password" binding:"required"`
}

type USERITEM struct {
	USER string `json:"user" binding:"required"`
	ITEM int64  `json:"item_id" binding:"required"`
}

type USERITEMSHOP struct {
	USER string `json:"user" binding:"required"`
	ITEM int64  `json:"item_id" binding:"required"`
	SHOP int64  `json:"shop_id" binding:"required"`
}

type User struct {
	Username      string
	Authenticated bool
}

var store *sessions.CookieStore

//initialize session management
func initSessionManagement() {
	authKeyOne := securecookie.GenerateRandomKey(64)
	encryptionKeyOne := securecookie.GenerateRandomKey(32)

	store = sessions.NewCookieStore(
		authKeyOne,
		encryptionKeyOne,
	)

	store.Options = &sessions.Options{
		Path:     "/",
		MaxAge:   60 * 20 * 10,
		HttpOnly: true,
	}

	gob.Register(User{})
}

func getUser(s *sessions.Session) User {
	val := s.Values["user"]
	var user = User{}
	user, ok := val.(User)
	if !ok {
		return User{Authenticated: false}
	}
	return user
}

// func mySessionHandler(c *gin.Context) {
// 	session, err := store.Get(c.Request, "session-name")
// 	if err != nil {
// 		//handle error
// 		log.Println("Failed to get session: %v", err)
// 	}

// }

//c.getRawData for post methods
//c.bindJson
func signIn(userClient userServicePackage.UserServiceClient) gin.HandlerFunc {
	return func(c *gin.Context) {
		var login LOGIN
		c.BindJSON(&login)

		res, err := userClient.ReadUser(context.Background(), &userServicePackage.ReadUserRequest{
			UserProfile: &userServicePackage.UserProfile{
				UserName: login.USER,
				Pw:       login.PASSWORD,
			},
		})

		if err != nil {
			log.Println("Failed to sign in user due to error: %v", err)
		}

		session, err1 := store.Get(c.Request, "session-name")
		if err1 != nil {
			log.Println("Cant get session from store due to error: %v", err1)
		}
		//successful sign in then add session token
		if res.Incorrect == -1 {
			user := &User{
				Username:      login.USER,
				Authenticated: true,
			}

			session.Values["user"] = user

			sessionErr := session.Save(c.Request, c.Writer)

			if sessionErr != nil {
				log.Println("Failed to save session token due to error: %v", sessionErr)
			}
		}

		c.JSON(http.StatusOK, gin.H{
			"message":   "sign-in",
			"username":  res.UserName,
			"incorrect": res.Incorrect,
		})
	}

}

//what should i do with session in sign up?
//post
func signUp(userClient userServicePackage.UserServiceClient) gin.HandlerFunc {
	return func(c *gin.Context) {
		var signup LOGIN
		c.BindJSON(&signup)

		res, err := userClient.CreateUser(context.Background(), &userServicePackage.CreateUserRequest{
			NewUserProfile: &userServicePackage.UserProfile{
				UserName: signup.USER,
				Pw:       signup.PASSWORD,
			},
		})

		if err != nil {
			log.Println("Failed to sign up user due to error: %v", err)
		}

		// session, err1 := store.Get(c.Request, "session-name")
		// if err1 != nil {
		// 	log.Println("Cant get session from store due to error: %v", err1)
		// }

		// if res.Duplicate == -1 {
		// 	user := &User{
		// 		Username:      signup.USER,
		// 		Authenticated: true,
		// 	}

		// 	session.Values["user"] = user

		// 	sessionErr := session.Save(c.Request, c.Writer)

		// 	if sessionErr != nil {
		// 		log.Println("Failed to save session token due to error: %v", sessionErr)
		// 	}
		// }

		c.JSON(http.StatusOK, gin.H{
			"message":   "sign-up",
			"username":  res.UserName,
			"duplicate": res.Duplicate,
		})
	}
}

//post
func logOut(c *gin.Context) {
	session, err := store.Get(c.Request, "session-name")
	if err != nil {
		log.Println("Cant get session from store due to error: %v", err)
	}

	session.Values["user"] = User{}
	session.Options.MaxAge = -1

	err = session.Save(c.Request, c.Writer)
	c.JSON(http.StatusOK, gin.H{
		"message": "log-out",
	})
}

//get
func signedIn(c *gin.Context) {
	session, err := store.Get(c.Request, "session-name")
	if err != nil {
		log.Println("Cant get session from store due to error: %v", err)
	}

	user := getUser(session)

	if auth := user.Authenticated; !auth {
		c.JSON(http.StatusOK, gin.H{
			"message":       "not authenticated",
			"authenticated": -1,
		})
	} else {
		c.JSON(http.StatusOK, gin.H{
			"message":       "checked sign in",
			"authenticated": 1,
		})
	}

}

//post
func deleteItem(userClient userServicePackage.UserServiceClient) gin.HandlerFunc {
	return func(c *gin.Context) {
		var useritem USERITEM
		c.BindJSON(&useritem)

		session, sessionErr := store.Get(c.Request, "session-name")
		if sessionErr != nil {
			log.Println("Cant get session from store due to error: %v", sessionErr)
		}

		user := getUser(session)

		if auth := user.Authenticated; !auth {
			c.JSON(http.StatusOK, gin.H{
				"message":       "not authenticated",
				"item_id":       -1,
				"notfound":      -1,
				"authenticated": -1,
			})

		} else {
			session.Options.MaxAge = 60 * 20 * 10

			error1 := session.Save(c.Request, c.Writer)
			if error1 != nil {
				log.Println("failed to save session")
			}
			res, err := userClient.DeleteItem(context.Background(), &userServicePackage.DeleteItemRequest{
				Useritem: &userServicePackage.UserItem{
					UserName: useritem.USER,
					ItemId:   useritem.ITEM,
				},
			})

			if err != nil {
				log.Println("Failed to delete item due to error: %v", err)
			}

			c.JSON(http.StatusOK, gin.H{
				"message":       "delete item",
				"item_id":       res.ItemId,
				"notfound":      res.NotFound,
				"authenticated": 1,
			})
		}

	}
}

//post
func addItem(userClient userServicePackage.UserServiceClient, priceClient priceServicePackage.PriceServiceClient) gin.HandlerFunc {
	return func(c *gin.Context) {
		var useritemshop USERITEMSHOP
		c.BindJSON(&useritemshop)

		session, sessionErr := store.Get(c.Request, "session-name")
		if sessionErr != nil {
			log.Println("Cant get session from store due to error: %v", sessionErr)
		}

		user := getUser(session)

		if auth := user.Authenticated; !auth {
			c.JSON(http.StatusOK, gin.H{
				"message":       "not authenticated",
				"item_id":       -1,
				"notfound":      -1,
				"duplicate":     -1,
				"authenticated": -1,
			})
		} else {

			session.Options.MaxAge = 60 * 20 * 10

			error1 := session.Save(c.Request, c.Writer)
			if error1 != nil {
				log.Println("failed to save session")
			}

			res, err := priceClient.CreateItemDetailPrice(context.Background(), &priceServicePackage.CreateItemDetailPriceRequest{
				ItemId: useritemshop.ITEM,
				ShopId: useritemshop.SHOP,
			})

			log.Println(useritemshop.ITEM)

			if err != nil {
				log.Println("Failed to add item in price service due to error: %v", err)
			}

			if res.Success == -1 {
				c.JSON(http.StatusOK, gin.H{
					"message":       "add item failed as item is not found in shopee",
					"item_id":       useritemshop.ITEM,
					"notfound":      1,
					"duplicate":     -1,
					"authenticated": 1,
				})
			} else {
				res1, err1 := userClient.CreateItem(context.Background(), &userServicePackage.AddItemRequest{
					UserItem: &userServicePackage.UserItem{
						UserName: useritemshop.USER,
						ItemId:   useritemshop.ITEM,
					},
				})

				if err1 != nil {
					log.Println("Failed to add item in user service due to error: %v", err1)
				}

				c.JSON(http.StatusOK, gin.H{
					"message":       "add item",
					"item_id":       useritemshop.ITEM,
					"notfound":      -1,
					"duplicate":     res1.Duplicate,
					"authenticated": 1,
				})
			}
		}

	}
}

//get
func getItemList(userClient userServicePackage.UserServiceClient, priceClient priceServicePackage.PriceServiceClient) gin.HandlerFunc {
	return func(c *gin.Context) {
		username := c.Query("username")
		limit := c.Query("limit")
		offset := c.Query("offset")

		session, sessionErr := store.Get(c.Request, "session-name")
		if sessionErr != nil {
			log.Println("Cant get session from store due to error: %v", sessionErr)
		}

		user := getUser(session)

		if auth := user.Authenticated; !auth {
			c.JSON(http.StatusOK, gin.H{
				"message":       "not authenticated",
				"username":      nil,
				"data":          nil,
				"empty":         -1,
				"authenticated": -1,
			})
		} else {
			session.Options.MaxAge = 60 * 20 * 10

			error1 := session.Save(c.Request, c.Writer)
			if error1 != nil {
				log.Println("failed to save session")
			}

			res, err := userClient.ReadAllItem(context.Background(), &userServicePackage.ReadAllListRequest{
				UserName: username,
				Limit:    StringToInt(limit),
				Offset:   StringToInt(offset),
			})

			if err != nil {
				log.Println("Read item list for user failed: %v", err)
			}

			if res.Empty == 1 {
				c.JSON(http.StatusOK, gin.H{
					"message":       "getItemList empty",
					"username":      username,
					"data":          res.ItemId,
					"empty":         res.Empty,
					"authenticated": 1,
				})
			} else {
				res1, err1 := priceClient.ReadItemInfo(context.Background(), &priceServicePackage.ReadItemInfoRequest{
					ItemId: res.ItemId,
				})

				if err1 != nil {
					log.Println("Read item info from price service failed: %v", err1)
				}

				c.JSON(http.StatusOK, gin.H{
					"message":       "getItemList",
					"username":      username,
					"data":          res1.ItemDetails,
					"empty":         -1,
					"authenticated": 1,
				})
			}

		}

	}
}

//get
func getPriceLog(priceClient priceServicePackage.PriceServiceClient) gin.HandlerFunc {
	return func(c *gin.Context) {

		itemid := c.Query("item_id")

		session, sessionErr := store.Get(c.Request, "session-name")
		if sessionErr != nil {
			log.Println("Cant get session from store due to error: %v", sessionErr)
		}

		user := getUser(session)

		if auth := user.Authenticated; !auth {
			c.JSON(http.StatusOK, gin.H{
				"message":       "not authenticated",
				"item_id":       -1,
				"data":          nil,
				"authenticated": -1,
			})
		} else {
			session.Options.MaxAge = 60 * 20 * 10

			error1 := session.Save(c.Request, c.Writer)
			if error1 != nil {
				log.Println("failed to save session")
			}
			res, err := priceClient.ReadPriceChange(context.Background(), &priceServicePackage.ReadPriceChangeRequest{
				ItemId: StringToInt(itemid),
			})

			if err != nil {
				log.Println("Read Price Change for item failed: %v", err)
			}

			c.JSON(http.StatusOK, gin.H{
				"message":       "getPriceChangeLog",
				"item_id":       itemid,
				"data":          res.List,
				"authenticated": 1,
			})

		}

	}
}

// StringToInt string to int function
func StringToInt(s string) int64 {
	i, _ := strconv.ParseInt(s, 10, 64)
	return i
}

func main() {

	//sessions.Default(c).Options(sessions.Option{MaxAge: nSeconds}) [for session in gin/sessions]

	log.Println("starting api gateway server...")

	var opts []grpc.DialOption

	opts = append(opts, grpc.WithInsecure())

	priceConn, err1 := grpc.Dial(*priceServiceGrpcAddr, opts...)

	if err1 != nil {
		log.Fatalf("did not connect to price server: %v", err1)
	}

	defer priceConn.Close()

	userConn, err2 := grpc.Dial(*userServiceGrpcAddr, opts...)

	if err2 != nil {
		log.Fatalf("did not connect to user server: %v", err2)
	}

	defer userConn.Close()

	initSessionManagement()

	priceClient := priceServicePackage.NewPriceServiceClient(priceConn)
	userClient := userServicePackage.NewUserServiceClient(userConn)

	router := gin.Default()

	config := cors.DefaultConfig()
	config.AllowOrigins = []string{"http://localhost:80"}
	config.AllowCredentials = true
	router.Use(cors.New(config))

	p := ginprometheus.NewPrometheus("gin")

	//what other label mappings do i need?
	p.ReqCntURLLabelMappingFn = func(c *gin.Context) string {
		url := c.Request.URL.Path
		// if c.Query("username") != "" {
		// 	url = strings.Replace(url, c.Query("username"), "username", 1)
		// }
		// if c.Query("offset") != "" {
		// 	url = strings.Replace(url, c.Query("offset"), "0", 1)
		// }
		// if c.Query("item_id") != "" {
		// 	url = strings.Replace(url, c.Query("item_id"), "123", 1)
		// }
		return url
	}

	p.Use(router)

	//user service
	router.POST("/api/sign-in", signIn(userClient))
	router.POST("/api/sign-up", signUp(userClient))
	router.POST("/api/log-out", logOut)
	router.POST("/api/delete-item", deleteItem(userClient))

	//user service and price service
	router.POST("/api/add-item", addItem(userClient, priceClient))
	router.GET("/api/item-list", getItemList(userClient, priceClient))

	//price service
	router.GET("/api/get-price-change-log", getPriceLog(priceClient))

	router.GET("/api/signed-in", signedIn)

	router.Run(*httpAddr)

}
