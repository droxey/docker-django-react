FROM postgres:10.1

ADD init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh
RUN chmod 0755 /docker-entrypoint-initdb.d/init-user-db.sh
RUN echo "host all  all    0.0.0.0/0  md5" >> /var/lib/postgresql/pg_hba.conf
RUN echo "listen_addresses='*'" >> /var/lib/postgresql/postgresql.conf
