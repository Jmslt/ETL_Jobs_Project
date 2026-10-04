# coding: utf-8
# %load conn_1.py
# %load conn_1.py
import pandas as pd
from sqlalchemy import create_engine, text


user = 'sa'
password = 'Admin12345!'
host = '127.0.0.1'
port = 1433
database_source = 'test1_db'
conn_string = f"mssql+pyodbc://{user}:{password}@{host}:{port}/{database_source}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

source_engine = create_engine(conn_string)

query1 = """
    INSERT INTO table1
    VALUES (3, 'bash')
"""

query2 = """
    SELECT *
    FROM table1
"""

with source_engine.connect() as conn :
    conn.execute(text(query1))
    conn.commit()
    result = conn.execute(text(query2))
    df = pd.DataFrame(result.fetchall(), columns=result.keys())

    print(df)
