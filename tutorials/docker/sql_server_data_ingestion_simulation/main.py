import pyodbc
import os
import sys
import logging
from typing import List
from datetime import datetime
from dotenv import load_dotenv

def get_connection_string() -> str:
    conn_str = (
        f'DRIVER={{{os.getenv("SQL_SERVER_DRIVER")}}};'
        f'SERVER={os.getenv("SQL_SERVER_HOST")};'
        f'DATABASE={os.getenv("SQL_SERVER_DATABASE")};'
        f'UID={os.getenv("SQL_SERVER_USERNAME")};'
        f'PWD={os.getenv("SQL_SERVER_PASSWORD")};'
        f'ENCRYPT={"yes" if os.getenv("SQL_SERVER_ENCRYPT", "True").upper() == "TRUE" else "no"};'
    )
    return conn_str

def get_project_data() -> List[dict]:
    return [
        {
            "name": "Initial DevOps Pipeline",
            "created_date": datetime(year = 2023, month = 10, day = 3).date()
        },
        {
            "name": "Python Version Upgrade Testing",
            "created_date": datetime(year = 2023, month = 9, day = 15).date()
        },
        {
            "name": "Stakeholder Survey Report",
            "created_date": datetime(year = 2023, month = 9, day = 28).date()
        }
    ]

def main():
    # Collect environment variables from .env file
    load_dotenv()

    # Collect data
    project_data = get_project_data()

    # Transform dictionary to tuple for bulk insert
    records = [(row.get("name"), row.get("created_date")) for row in project_data] 

    # Establish connection to SQL Server
    try:
        connection = pyodbc.connect(
            get_connection_string()
        )
    except Exception as conn_err:
        logging.error(conn_err.args)
        sys.exit(1)   

    # Attempt to bulk insert into SQL Server table
    cursor = connection.cursor()
    cursor.fast_executemany = True
    try:
        cursor.executemany(
            'INSERT INTO [dbo].[projects] (Name, Created_Date) VALUES (?, ?)',
            records
        )
        cursor.commit()
    except Exception as query_err:
        logging.error(query_err.args)
    cursor.close()


if __name__ == "__main__":
    main()