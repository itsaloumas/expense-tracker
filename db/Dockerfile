FROM mariadb:latest

ENV MARIADB_ROOT_PASSWORD=my-secret-pw \
    MARIADB_DATABASE=expense_db \
    MARIADB_USER=user \
    MARIADB_PASSWORD=userpass

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
