package userServicePackage

import (
	"context"
	"database/sql"
	"fmt"
	"log"

	"github.com/go-sql-driver/mysql"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"

	"golang.org/x/crypto/bcrypt"

	userServicePackage "git.garena.com/simun.tham/entry-task/grpc-user-microservice/pkg/api"
)

type UserServiceServer struct {
	db *sql.DB
}

// NewUserServiceServer creates User service
func NewUserServiceServer(db *sql.DB) userServicePackage.UserServiceServer {
	return &UserServiceServer{db: db}
}

// connect returns SQL database connection from the pool
func (s *UserServiceServer) connect(ctx context.Context) (*sql.DB, error) {
	// c, err := s.db.Conn(ctx)
	// if err != nil {
	// 	return nil, status.Error(codes.Unknown, "failed to connect to database-> "+err.Error())
	// }
	// return c, nil
	return s.db, nil
}

func hashAndSalt(pwd []byte) string {

	// Use GenerateFromPassword to hash & salt pwd
	// MinCost is just an integer constant provided by the bcrypt
	// package along with DefaultCost & MaxCost.
	// The cost can be any value you want provided it isn't lower
	// than the MinCost (4)
	hash, err := bcrypt.GenerateFromPassword(pwd, bcrypt.MinCost)
	if err != nil {
		log.Println(err)
	}
	// GenerateFromPassword returns a byte slice so we need to
	// convert the bytes to a string and return it
	return string(hash)
}

func comparePasswords(hashedPwd string, plainPwd []byte) bool {
	// Since we'll be getting the hashed password from the DB it
	// will be a string so we'll need to convert it to a byte slice
	byteHash := []byte(hashedPwd)
	err := bcrypt.CompareHashAndPassword(byteHash, plainPwd)
	if err != nil {
		log.Println(err)
		return false
	}

	return true
}

// Create new user
func (s *UserServiceServer) CreateUser(ctx context.Context, req *userServicePackage.CreateUserRequest) (*userServicePackage.CreateUserResponse, error) {

	// get SQL connection from pool
	c, err := s.connect(ctx)
	if err != nil {
		return nil, err
	}
	// defer c.Close()

	pw := req.NewUserProfile.Pw
	//hashing and salt pw
	var hashedPw string = hashAndSalt([]byte(pw))

	// insert UserProfile entity data
	res, err := c.ExecContext(ctx, "INSERT INTO UserProfile(`user_name`, `password`) VALUES(?, ?)",
		req.NewUserProfile.UserName, hashedPw)

	if err != nil {
		me := err.(*mysql.MySQLError)
		//for duplicate entry
		if me.Number == 1062 {
			//duplicate user name
			return &userServicePackage.CreateUserResponse{
				UserName:  req.NewUserProfile.UserName,
				Duplicate: 1,
			}, nil
		} else {
			return nil, status.Error(codes.Unknown, "failed to insert user into UserProfile-> "+err.Error())
		}
	}

	// get user_id of created user
	id, err := res.LastInsertId()
	if err != nil {
		return nil, status.Error(codes.Unknown, "failed to retrieve id for created user-> "+err.Error())
	}

	log.Println(id)

	return &userServicePackage.CreateUserResponse{
		UserName:  req.NewUserProfile.UserName,
		Duplicate: -1,
	}, nil
}

// Read user
func (s *UserServiceServer) ReadUser(ctx context.Context, req *userServicePackage.ReadUserRequest) (*userServicePackage.ReadUserResponse, error) {
	// get SQL connection from pool
	c, err := s.connect(ctx)
	if err != nil {
		return nil, err
	}
	// defer c.Close()

	// query UserProfile by user_id
	rows, err := c.QueryContext(ctx, "SELECT `id`, `user_name`, `password` FROM UserProfile WHERE `user_name`=?",
		req.UserProfile.UserName)

	if err != nil {
		return nil, status.Error(codes.Unknown, "failed to select from UserProfile-> "+err.Error())
	}
	defer rows.Close()

	if !rows.Next() {
		if err := rows.Err(); err != nil {
			return nil, status.Error(codes.Unknown, "failed to retrieve data from UserProfile-> "+err.Error())
		}
		return &userServicePackage.ReadUserResponse{
			UserName:  req.UserProfile.UserName,
			Incorrect: 1,
		}, nil
	}

	// get User hashed password data if there is a username found

	var id int64
	var userName string
	var password string

	if err := rows.Scan(&id, &userName, &password); err != nil {
		return nil, status.Error(codes.Unknown, "failed to retrieve field values from UserProfile row-> "+err.Error())
	}

	if rows.Next() {
		return nil, status.Error(codes.Unknown, fmt.Sprintf("found multiple user profile rows with username '%s'",
			req.UserProfile.UserName))
	}

	if !comparePasswords(password, []byte(req.UserProfile.Pw)) {
		return &userServicePackage.ReadUserResponse{
			UserName:  userName,
			Incorrect: 1,
		}, nil
	}

	return &userServicePackage.ReadUserResponse{
		UserName:  userName,
		Incorrect: -1,
	}, nil
}

// Create new item (add item to list for user)
func (s *UserServiceServer) CreateItem(ctx context.Context, req *userServicePackage.AddItemRequest) (*userServicePackage.AddItemResponse, error) {

	// get SQL connection from pool
	c, err := s.connect(ctx)
	if err != nil {
		return nil, err
	}
	// defer c.Close()

	rows, err := c.QueryContext(ctx, "SELECT * FROM UserItems WHERE `user_name`=? AND `item_id`=? AND `deleted`=1", req.UserItem.UserName, req.UserItem.ItemId)

	defer rows.Close()

	// var list []int64
	// var item_id int64
	// for result.Next() {
	// 	if err := rows.Scan(&item_id); err != nil {
	// 		return nil, status.Error(codes.Unknown, "failed to retrieve field values from UserItems row-> "+err.Error())
	// 	}
	// 	list.append(item_id)
	// }

	if rows.Next() {
		c1, err := s.connect(ctx)
		if err != nil {
			return nil, err
		}
		// defer c1.Close()

		res, err := c1.ExecContext(ctx, "UPDATE UserItems SET `deleted`=NULL WHERE `user_name`=? AND `item_id`=?", req.UserItem.UserName, req.UserItem.ItemId)
		if err != nil {
			return nil, status.Error(codes.Unknown, "failed to update table->"+err.Error())
		}
		log.Println(res)
		return &userServicePackage.AddItemResponse{
			ItemId:    req.UserItem.ItemId,
			Duplicate: -1,
		}, nil
	}

	c2, err := s.connect(ctx)
	if err != nil {
		return nil, err
	}
	// defer c2.Close()

	// insert UserProfile entity data
	res, err := c2.ExecContext(ctx, "INSERT INTO UserItems(`user_name`, `item_id`) VALUES(?, ?)",
		req.UserItem.UserName, req.UserItem.ItemId)

	if err != nil {
		me := err.(*mysql.MySQLError)
		//for duplicate entry
		if me.Number == 1062 {
			//duplicate user name and item_id handling
			return &userServicePackage.AddItemResponse{
				ItemId:    req.UserItem.ItemId,
				Duplicate: 1,
			}, nil
		} else {
			return nil, status.Error(codes.Unknown, "failed to insert item id into UserItems-> "+err.Error())
		}
	}

	// get id of created item
	id, err := res.LastInsertId()
	if err != nil {
		return nil, status.Error(codes.Unknown, "failed to retrieve id for created user-> "+err.Error())
	}

	log.Println(id)

	return &userServicePackage.AddItemResponse{
		ItemId:    req.UserItem.ItemId,
		Duplicate: -1,
	}, nil
}

// Delete item (delete item from list for user)
func (s *UserServiceServer) DeleteItem(ctx context.Context, req *userServicePackage.DeleteItemRequest) (*userServicePackage.DeleteItemResponse, error) {

	// get SQL connection from pool
	c, err := s.connect(ctx)
	if err != nil {
		return nil, err
	}
	// defer c.Close()

	// insert UserProfile entity data
	res, err := c.ExecContext(ctx, "UPDATE UserItems SET deleted = 1 WHERE user_name = ? AND item_id = ?",
		req.Useritem.UserName, req.Useritem.ItemId)

	if err != nil {
		return nil, status.Error(codes.Unknown, "failed to delete item id for user-> "+err.Error())
	}

	rows, err := res.RowsAffected()
	if err != nil {
		return nil, status.Error(codes.Unknown, "failed to retrieve rows affected value-> "+err.Error())
	}

	if rows == 0 {
		return &userServicePackage.DeleteItemResponse{
			ItemId:   req.Useritem.ItemId,
			NotFound: 1,
		}, nil
	}

	return &userServicePackage.DeleteItemResponse{
		ItemId:   req.Useritem.ItemId,
		NotFound: -1,
	}, nil
}

// Read all item_id list for user
func (s *UserServiceServer) ReadAllItem(ctx context.Context, req *userServicePackage.ReadAllListRequest) (*userServicePackage.ReadAllListResponse, error) {

	// get SQL connection from pool
	c, err := s.connect(ctx)
	if err != nil {
		return nil, err
	}
	// defer c.Close()

	// get item list
	rows, err := c.QueryContext(ctx, "SELECT `id`, `user_name`, `item_id` FROM UserItems WHERE `user_name`=? AND `deleted` IS NULL LIMIT ? OFFSET ?", req.UserName, req.Limit, req.Offset)
	if err != nil {
		return nil, status.Error(codes.Unknown, "failed to select from UserItems-> "+err.Error())
	}
	defer rows.Close()

	var id int64
	var user_name string
	var item_id int64
	var list []int64

	for rows.Next() {
		if err := rows.Scan(&id, &user_name, &item_id); err != nil {
			return nil, status.Error(codes.Unknown, "failed to retrieve field values from UserItems row-> "+err.Error())
		}

		list = append(list, item_id)
	}

	if err := rows.Err(); err != nil {
		return nil, status.Error(codes.Unknown, "failed to retrieve data from UserItems-> "+err.Error())
	}

	if len(list) == 0 {
		list = append(list, -1)
		return &userServicePackage.ReadAllListResponse{
			ItemId: list,
			Empty:  1,
		}, nil

	}

	return &userServicePackage.ReadAllListResponse{
		ItemId: list,
		Empty:  -1,
	}, nil
}
