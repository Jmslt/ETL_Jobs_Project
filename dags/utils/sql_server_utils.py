from sqlalchemy import create_engine, text
import pyarrow as pa
import mssql_python

def generate_conn_string(db):
    user = "sa"
    password = "Admin12345!"
    host = "sql_tfe"
    port = 1433
    database_source = db
    generated_conn_string = f"mssql+pyodbc://{user}:{password}@{host}:{port}/{database_source}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
    return generated_conn_string


def create_sqlserver_engine(conn_string, fast=False):
    if fast is True:
        #TODO check if possible with cursor
        source_engine = create_engine(conn_string, fast_executemany=True)
    elif fast is False:
        source_engine = create_engine(conn_string)
    return source_engine

