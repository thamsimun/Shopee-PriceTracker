package main

import (
	"fmt"
	"os"

	"git.garena.com/simun.tham/entry-task/grpc-user-microservice/pkg/cmd"
)

func main() {
	if err := cmd.RunServer(); err != nil {
		fmt.Fprintf(os.Stderr, "%v\n", err)
		os.Exit(1)
	}
}
