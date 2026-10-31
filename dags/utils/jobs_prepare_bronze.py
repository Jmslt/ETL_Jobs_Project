# coding: utf-8
import polars as pl

import os

from utils.schema_override_jobs import list_columns_complete, get_schema_jobs_pl, get_schema_nolist
from utils.sql_server_utils import generate_conn_string, create_sqlserver_engine


LIST_COL = ["countries", "skills", "cities", "company_industries", "company_types", "company_sizes", "domains"]
LIST_TABLES = ["countries", "skills", "cities", "company_industries", "company_types", "company_sizes", "company_domains"]


def create_postings_df(file, offset):
    df_postings = pl.read_ndjson(file.path, row_index_name="job_id", row_index_offset=offset, ignore_errors=True)
    return df_postings


def create_col_df(df):
    dict_tables = {}
    for number, column in enumerate(LIST_COL):
        dict_tables[column] = (df.select("job_id", column)
                                .explode(column, empty_as_null=True))
        dict_tables[column].table = "dbo.jobs_" + LIST_TABLES[number]
    return dict_tables


def load_cols_to_db(dict_df, fast_param):
    conn_string = generate_conn_string("bronze_tfe")
    sql_engine = create_sqlserver_engine(conn_string, fast=fast_param)
    for df_name, df in dict_df.items():
        print(f"Writing table {df.table} to DB")
        df.write_database(table_name=df.table, connection=sql_engine, if_table_exists="append")

def load_postings_to_db(file, fast_param, offset):
    conn_string = generate_conn_string("bronze_tfe")
    sql_engine = create_sqlserver_engine(conn_string, fast=fast_param)
    schema_complete = get_schema_jobs_pl()
    schema_no_list = get_schema_nolist(schema_complete)
    print("Writing jobs_posting table to DB")
    df_postings = pl.read_ndjson(file.path, schema=schema_no_list, row_index_offset= offset, row_index_name="job_id",ignore_errors=True)
    new_offset = df_postings.select("job_id").max().item() + 1
    print(f"Current offset: {new_offset}")
    df_postings.write_database(table_name="jobs_postings", connection=sql_engine, if_table_exists="append")
    return new_offset


def load_jobs_to_bronze(fast_param):
    current_offset = 0
    
    for file in os.scandir("data/jobs/"):
        postings_df = create_postings_df(file, current_offset)
        dict_df = create_col_df(postings_df)
        load_cols_to_db(dict_df, fast_param)
        current_offset = load_postings_to_db(file, fast_param, current_offset)

