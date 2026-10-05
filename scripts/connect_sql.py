# coding: utf-8
from sqlalchemy import create_engine, text
user = "ICT-210-06\DE2026"
password = ""
host = user
user = "ICT-210-06\stgadmin"
port = 1433
conn_string = f"mssql+pyodbc://{user}:{password}@{host}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
password = "Test!1234="
source_engine = create_engine(conn_string)
