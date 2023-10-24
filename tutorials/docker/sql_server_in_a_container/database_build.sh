#!/bin/bash

MSSQL_HOST="localhost"
MSSQL_SA_USERNAME="sa"

for i in {1..50}:
do
    echo "Attemping to initialize SQL Server database"
    /opt/mssql-tools/bin/sqlcmd \
        -S ${MSSQL_HOST} \
        -U ${MSSQL_SA_USERNAME} \
        -P ${MSSQL_SA_PASSWORD} \
        -d master \
        -Q 'CREATE DATABASE business_db'

    if [ $? -eq 0 ]
    then
        echo "Creating tables..."
        /opt/mssql-tools/bin/sqlcmd \
            -S ${MSSQL_HOST} \
            -U ${MSSQL_SA_USERNAME} \
            -P ${MSSQL_SA_PASSWORD} \
            -d business_db \
            -i/db_setup/database_init.sql

        echo "SQL Server database is operational"
        while true
        do
            sleep 1
        done
    else
        sleep 1
    fi
done