# Install the base requirements for the app.
# This stage is to support development.
FROM golang:1.12
WORKDIR /app/api-gateway
COPY . .
RUN go mod download
RUN go build .
CMD ["./api-gateway"]





