import polars as pl
import os

from utils.schema_override_jobs import list_columns, get_schema_jobs_pl
from utils.sql_server_utils import generate_conn_string, create_sqlserver_engine


def create_pl_df(file):
    schema_str = get_schema_jobs_pl()
    pl_df = pl.read_ndjson(file, schema=schema_str)
    return pl_df

def pl_write_to_bronze(df):
    conn = generate_conn_string()
    engine = create_sqlserver_engine(conn)
    df.write_database(table_name="dbo.jobs_data", connection=engine, if_table_exists="append")


if __name__ == "__main__":
    for file in os.scandir("/home/jm/projects/tfe/jobs_data_valid"):
        print(f"Writing file {file.name} to DB")
        schema_str = get_schema_jobs_pl()
        df_to_write = create_pl_df(file.path)
        pl_write_to_bronze(df_to_write)

print("Loading over.")



#TODO Find a way to actually get nvarchar with polars
#df_nvarchar = df_string.with_columns(skills=pl.col().str.normalize("NFKC"))
#df_nvarchar = df_string.with_columns(description=pl.col("description").str.normalize("NFKC"))
#df_nvarchar = df_nvarchar.top_k(10000, by="public_slug")

#df_nvarchar.write_database(table_name="dbo.jobs_data", connection=conn, if_table_exists="append")

