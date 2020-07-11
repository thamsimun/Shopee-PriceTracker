# Install the base requirements for the app.
# This stage is to support development.
FROM python:2.7
WORKDIR /app/price
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get -q update && apt-get -qy install netcat
RUN chmod 777 ./commands.sh
# CMD ["./commands.sh"]






