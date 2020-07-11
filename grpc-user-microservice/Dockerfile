# Install the base requirements for the app.
# This stage is to support development.
FROM golang:1.12
WORKDIR /app/user
COPY . .
RUN  go mod download
RUN go build ./cmd/server
RUN apt-get -q update && apt-get -qy install netcat
# CMD ["./cmd/server/server"]





