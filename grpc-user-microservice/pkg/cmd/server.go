package cmd

import (
	"context"
	"database/sql"
	"flag"
	"fmt"

	// mysql driver
	_ "github.com/go-sql-driver/mysql"

	"git.garena.com/simun.tham/entry-task/grpc-user-microservice/pkg/protocol/grpc"
	userServicePackage "git.garena.com/simun.tham/entry-task/grpc-user-microservice/pkg/service"
)

// Config is configuration for Server
type Config struct {
	// gRPC server start parameters section
	// gRPC is TCP port to listen by gRPC server
	GRPCPort string

	// DB Datastore parameters section
	// DatastoreDBHost is host of database
	DatastoreDBHost string
	// DatastoreDBUser is username to connect to database
	DatastoreDBUser string
	// DatastoreDBPassword password to connect to database
	DatastoreDBPassword string
	// DatastoreDBSchema is schema of database
	DatastoreDBSchema string
}

// RunServer runs gRPC server and HTTP gateway
func RunServer() error {
	ctx := context.Background()

	// get configuration
	var cfg Config
	flag.StringVar(&cfg.GRPCPort, "grpc-port", "50051", "gRPC port to bind")
	flag.StringVar(&cfg.DatastoreDBHost, "db-host", "db:3306", "Database host")
	flag.StringVar(&cfg.DatastoreDBUser, "db-user", "root", "Database user")
	flag.StringVar(&cfg.DatastoreDBPassword, "db-password", "Garena.com", "Database password")
	flag.StringVar(&cfg.DatastoreDBSchema, "db-schema", "User", "Database schema")

	if len(cfg.GRPCPort) == 0 {
		return fmt.Errorf("invalid TCP port for gRPC server: '%s'", cfg.GRPCPort)
	}

	// add MySQL driver specific parameter to parse date/time
	// Drop it for another database
	param := "parseTime=true"

	dsn := fmt.Sprintf("%s:%s@tcp(%s)/%s?%s",
		cfg.DatastoreDBUser,
		cfg.DatastoreDBPassword,
		cfg.DatastoreDBHost,
		cfg.DatastoreDBSchema,
		param)
	db, err := sql.Open("mysql", dsn)
	db.SetMaxOpenConns(500)
	if err != nil {
		return fmt.Errorf("failed to open database: %v", err)
	}

	userServicePackageAPI := userServicePackage.NewUserServiceServer(db)

	return grpc.RunServer(ctx, userServicePackageAPI, cfg.GRPCPort)
}
