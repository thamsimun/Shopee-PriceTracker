package grpc

import (
	"context"
	"log"
	"net"
	"os"
	"os/signal"

	userServicePackage "git.garena.com/simun.tham/entry-task/grpc-user-microservice/pkg/api"
	"google.golang.org/grpc"
)

// RunServer runs gRPC service to publish User service
func RunServer(ctx context.Context, userServicePackageAPI userServicePackage.UserServiceServer, port string) error {
	listen, err := net.Listen("tcp", ":"+port)
	if err != nil {
		return err
	}

	var opts []grpc.ServerOption
	// register service
	server := grpc.NewServer(opts...)
	userServicePackage.RegisterUserServiceServer(server, userServicePackageAPI)

	// graceful shutdown
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt)
	go func() {
		for range c {
			// sig is a ^C, handle it
			log.Println("shutting down gRPC server...")

			server.GracefulStop()

			<-ctx.Done()
		}
	}()

	// start gRPC server
	log.Println("starting gRPC server...")
	return server.Serve(listen)
}
