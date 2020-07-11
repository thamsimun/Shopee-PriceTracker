package main

import (
	"context"
	"flag"
	"log"
	"time"

	userServicePackage "git.garena.com/simun.tham/entry-task/grpc-user-microservice/pkg/api"

	"google.golang.org/grpc"
)

func main() {
	// get configuration
	address := flag.String("server", "", "gRPC server in format host:port")
	flag.Parse()

	// Set up a connection to the server.
	conn, err := grpc.Dial(*address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	c := userServicePackage.NewUserServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	// // Call Create
	// req1 := userServicePackage.CreateUserRequest{
	// 	NewUserProfile: &userServicePackage.UserProfile{
	// 		UserName: "test",
	// 		Pw:       "test",
	// 	},
	// }
	// res1, err := c.CreateUser(ctx, &req1)
	// if err != nil {
	// 	log.Fatalf("Create user failed: %v", err)
	// }
	// log.Printf("Create user result: <%+v>\n\n", res1)

	// Read
	// req2 := userServicePackage.ReadUserRequest{
	// 	UserProfile: &userServicePackage.UserProfile{
	// 		UserName: "test",
	// 		Pw:       "test",
	// 	},
	// }
	// res2, err := c.ReadUser(ctx, &req2)
	// if err != nil {
	// 	log.Fatalf("Read user failed: %v", err)
	// }
	// log.Printf("Read user result: <%+v>\n\n", res2)

	// // Read with wrong pw
	// req3 := userServicePackage.ReadUserRequest{
	// 	UserProfile: &userServicePackage.UserProfile{
	// 		UserName: "test",
	// 		Pw:       "testtest",
	// 	},
	// }
	// res3, err := c.ReadUser(ctx, &req3)
	// if err != nil {
	// 	log.Fatalf("Read user failed: %v", err)
	// }
	// log.Printf("Read user result: <%+v>\n\n", res3)

	// Read with no such username
	// req4 := userServicePackage.ReadUserRequest{
	// 	UserProfile: &userServicePackage.UserProfile{
	// 		UserName: "testtest",
	// 		Pw:       "test",
	// 	},
	// }
	// res4, err := c.ReadUser(ctx, &req4)
	// if err != nil {
	// 	log.Fatalf("Read user failed: %v", err)
	// }
	// log.Printf("Read user result: <%+v>\n\n", res4)

	// // Call Create for a duplicate
	// req5 := userServicePackage.CreateUserRequest{
	// 	NewUserProfile: &userServicePackage.UserProfile{
	// 		UserName: "test",
	// 		Pw:       "test",
	// 	},
	// }
	// res5, err := c.CreateUser(ctx, &req5)
	// if err != nil {
	// 	log.Fatalf("Create user failed: %v", err)
	// }
	// log.Printf("Create user result: <%+v>\n\n", res5)

	// // Call Create item
	// req6 := userServicePackage.AddItemRequest{
	// 	UserItem: &userServicePackage.UserItem{
	// 		UserName: "test",
	// 		ItemId:   123,
	// 	},
	// }
	// res6, err := c.CreateItem(ctx, &req6)
	// if err != nil {
	// 	log.Fatalf("Create item failed: %v", err)
	// }
	// log.Printf("Create item result: <%+v>\n\n", res6)

	// // Call Create item
	// req7 := userServicePackage.AddItemRequest{
	// 	UserItem: &userServicePackage.UserItem{
	// 		UserName: "test",
	// 		ItemId:   122,
	// 	},
	// }
	// res7, err := c.CreateItem(ctx, &req7)
	// if err != nil {
	// 	log.Fatalf("Create item failed: %v", err)
	// }
	// log.Printf("Create item result: <%+v>\n\n", res7)

	// // Call ReadAll for list of times
	// req8 := userServicePackage.ReadAllListRequest{
	// 	UserName: "test",
	// 	Offset:   0,
	// 	Limit:    1,
	// }
	// res8, err := c.ReadAllItem(ctx, &req8)
	// if err != nil {
	// 	log.Fatalf("ReadAll failed: %v", err)
	// }
	// log.Printf("ReadAll result: <%+v>\n\n", res8)

	// // Delete item
	// req9 := userServicePackage.DeleteItemRequest{
	// 	Useritem: &userServicePackage.UserItem{
	// 		UserName: "test",
	// 		ItemId:   123,
	// 	},
	// }
	// res9, err := c.DeleteItem(ctx, &req9)
	// if err != nil {
	// 	log.Fatalf("Delete item failed: %v", err)
	// }
	// log.Printf("Delete item result: <%+v>\n\n", res9)

	// Call ReadAll for list of times
	req10 := userServicePackage.ReadAllListRequest{
		UserName: "simuntou",
		Offset:   2,
		Limit:    6,
	}
	res10, err := c.ReadAllItem(ctx, &req10)
	if err != nil {
		log.Fatalf("ReadAll failed: %v", err)
	}
	log.Printf("ReadAll result: <%+v>\n\n", res10)

	// // Delete item that is not found
	// req11 := userServicePackage.DeleteItemRequest{
	// 	Useritem: &userServicePackage.UserItem{
	// 		UserName: "test",
	// 		ItemId:   121,
	// 	},
	// }
	// res11, err := c.DeleteItem(ctx, &req11)
	// if err != nil {
	// 	log.Fatalf("Delete item failed: %v", err)
	// }
	// log.Printf("Delete item result: <%+v>\n\n", res11)

	// // Delete item but user not found
	// req12 := userServicePackage.DeleteItemRequest{
	// 	Useritem: &userServicePackage.UserItem{
	// 		UserName: "test2",
	// 		ItemId:   122,
	// 	},
	// }
	// res12, err := c.DeleteItem(ctx, &req12)
	// if err != nil {
	// 	log.Fatalf("Delete item failed: %v", err)
	// }
	// log.Printf("Delete item result: <%+v>\n\n", res12)

	// // Call ReadAll for list of times for user not found
	// req13 := userServicePackage.ReadAllListRequest{
	// 	UserName: "testtest",
	// }
	// res13, err := c.ReadAllItem(ctx, &req13)
	// if err != nil {
	// 	log.Fatalf("ReadAll failed: %v", err)
	// }
	// log.Printf("ReadAll result: <%+v>\n\n", res13)
}
