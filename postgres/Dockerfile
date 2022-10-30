FROM postgres:latest

# ENV POSTGRES_PASSWORD docker

RUN mkdir -p /docker-entrypoint-initdb.d
#COPY ./init-user-db.sh /docker-entrypoint-initdb.d

COPY ./init.sql ./docker-entrypoint-initdb.d

#RUN chmod +x /docker-entrypoint-initdb.d/init-user-db.sh
