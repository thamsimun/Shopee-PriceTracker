FROM mysql:8.0.20
ADD ./init/init.sql /docker-entrypoint-initdb.d/
RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/
VOLUME /docker-entrypoint-initdb.d
# RUN chmod 777 /docker-entrypoint-initdb.d
