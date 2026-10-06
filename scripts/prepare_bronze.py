import polars as pl
import pandas as pd

from utils.schema_override_jobs import list_columns, set_schema_jobs
from utils.sql_server_utils import generate_conn_string, create_sql_server_engine


SchemaStr = set_schema_jobs(list_columns)
lf = pl.scan_ndjson("/home/jm/projects/tfe/jobs_data_valid/freehire_jobs_part_003.jsonl", schema=SchemaStr)

lf.collect_schema()
conn = generate_conn_string()
engine = create_sqlserver_engine(conn)
#df = pl.read_ndjson("/home/jm/projects/tfe/jobs_data_valid/freehire_jobs_part_013.jsonl", schema=SchemaStr)
#df.write_database(table_name="dbo.jobs_data", connection=conn, if_table_exists="append")

df = pd.read_json("/home/jm/projects/tfe/jobs_data_valid/freehire_jobs_part_003.jsonl", lines=True,
                 dtype=SchemaStr)

#df.to_sql(name="jobs_data", if_exists="append", dtype=SchemaStr, index=False, con=engine)
