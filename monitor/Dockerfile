FROM quay.io/prometheus/prometheus:v2.0.0
ADD prometheus.yml /etc/prometheus/
RUN chown -R 472:472 /etc/prometheus/
VOLUME /etc/prometheus/prometheus.yml
# RUN chmod 777 /docker-entrypoint-initdb.d