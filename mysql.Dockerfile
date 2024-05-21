# Use the official MySQL Docker image as the base image
FROM mysql:latest

# Set environment variables for MySQL root user password and database name
ENV MYSQL_ROOT_PASSWORD=12345

# Copy SQL script to initialize the database and table
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port
EXPOSE 3306

VOLUME /lab-24-docker-mysql