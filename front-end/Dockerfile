# Install the base requirements for the app.
# This stage is to support development.
FROM nginx:alpine
COPY ./entry-task-app/build /var/www
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
ENTRYPOINT ["nginx","-g","daemon off;"]






