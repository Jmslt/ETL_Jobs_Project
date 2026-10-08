from sqlalchemy import create_engine, text
import pyarrow as pa
import mssql_python

def generate_conn_string(db):
    user = "sa"
    password = "Admin12345!"
    host = "localhost"
    port = 1435
    database_source = db
    generated_conn_string = f"mssql+pyodbc://{user}:{password}@{host}:{port}/{database_source}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
    return generated_conn_string


def create_sqlserver_engine(conn_string, autocommit=False):
    if autocommit is True:
        #TODO check if possible with cursor
        source_engine = create_engine(conn_string).execution_options(isolation_level="AUTOCOMMIT")
    elif autocommit is False:
        source_engine = create_engine(conn_string)
    return source_engine


def create_db(engine_with_autocommit_true, db_name):
    with engine_with_autocommit_true.connect() as conn:
        conn.execute(text(f"CREATE DATABASE [{db_name}]"))
#    conn.commit()
#    result = conn.execute(text(query2))
#    df = pd.DataFrame(result.fetchall(), columns=result.keys())

#    print(df)
