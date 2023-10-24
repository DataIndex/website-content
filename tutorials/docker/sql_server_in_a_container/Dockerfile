FROM mcr.microsoft.com/mssql/server:latest

WORKDIR /db_setup

USER root

# Install any necessary dependencies
RUN apt-get update && apt-get install -y \
    g++ \
    unixodbc-dev \
    gnupg \
    curl \
    apt-transport-https \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Add Microsoft's GPG key
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Add Microsoft's SQL Server Debian repository
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Install SQL Server drivers and SQL Server Command Line tools
RUN apt-get update \
    && ACCEPT_EULA=Y apt-get -y install msodbcsql17 mssql-tools \
    && rm -rf /var/lib/apt/lists/*

# Copy only necessary scripts into the container
COPY ./entrypoint.sh /db_setup/entrypoint.sh
COPY ./database_build.sh /db_setup/database_build.sh
COPY ./database_init.sql /db_setup/database_init.sql

# Set permissions for docker-entrypoint-db.sh
RUN chmod +x /db_setup/entrypoint.sh
RUN chmod +x /db_setup/database_build.sh

VOLUME /var/opt/mssql/data

# Run the command on container startup
ENTRYPOINT ["./entrypoint.sh"]