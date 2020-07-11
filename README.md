# Entry-task Price Tracking Application

## Deploy and Run
1. Build images and run the services containers:
    ```
    docker-compose up
    ```
2. Get containers details:
    ```
    docker container ls -a
    ```
3. View logs of each containers:
    ```
    docker-compose logs [container-name]
    ```
4. Stop running containers:
    ```
    docker-compose stop
    ```
5. Stop running and remove containers:
    ```
    docker-compose down
    ```
6. Rebuild containers:
    ```
    docker-compose build
    ```

## Ports 
1. Api-gateway: 8181:8181
2. User-service: 50051
3. Price-service: 8080
4. Database: 3306
5. Prometheus: 9090:9090
6. Grafana: 3000:3000
7. Cadvisor: 8282:8080

## To change ports
Edit docker-compose.yml to configure and edit prometheus.yml if necessary.

