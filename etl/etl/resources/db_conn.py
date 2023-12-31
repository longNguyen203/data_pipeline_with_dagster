from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os


def get_sql_connects():
    """ Return db connection """
    password = os.environ['PGPASS']
    userid = os.environ['PGUID']
    driver = "{ODBC Driver 17 for SQL Server}"
    server = "LongNguyen\LONGDEV"
    database = "AdventureWorksDW2019"

    connect = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={userid};PWD={password}")
    try:
        return connect
    except Exception as e:
        print(f"Error: {e}")


import pyodbc

def get_sql_connect():
    
    """ Return db connection """
    driver = "{ODBC Driver 17 for SQL Server}"
    server = "LongNguyen\LONGDEV"
    database = "AdventureWorksDW2019"
    
    connect = pyodbc.connect(driver=driver, host=server, database=database, trusted_connection="yes")
    
    try:
        return connect
    except Exception as e:
        print(f"Error: {e}")