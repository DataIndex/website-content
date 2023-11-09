FROM python:3.11-bullseye

USER root

WORKDIR /app

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
    && ACCEPT_EULA=Y apt-get -y install msodbcsql17 \
    && rm -rf /var/lib/apt/lists/*


# Add Microsoft's GPG key
#RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Add Microsoft's SQL Server Debian repository
#RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Install SQL Server drivers and SQL Server Command Line tools
#RUN apt-get update
#RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
#RUN apt-get install -y unixodbc-dev

COPY . .

RUN pip install -r requirements.txt

# Add and set permissions for docker-compose-wait
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.12.0/wait /wait
RUN chmod +x /wait

# Set permissions for entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]