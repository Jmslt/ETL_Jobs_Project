# coding: utf-8
import polars as pl

import os

from utils.schema_override_jobs import list_columns_complete, get_schema_jobs_pl, get_schema_nolist
from utils.sql_server_utils import generate_conn_string, create_sqlserver_engine


def load_to_bronze():
    file_nbr = 0
    current_offset = 0
    conn_string = generate_conn_string("bronze_tfe")
    sql_engine = create_sqlserver_engine(conn_string)
    for file in os.scandir("/home/jm/projects/tfe/jobs_data_sample/"):
        df_postings = pl.DataFrame()
        if file_nbr == 0:
            df_postings = pl.read_ndjson(file.path, row_index_name="job_id",
                                     ignore_errors=True)

        else:
            df_postings = pl.read_ndjson(file.path, ignore_errors=True)
            df_postings = df_postings.with_row_index("job_id", offset=current_offset)
        

        jobs_countries = df_postings.select("job_id","countries").explode("countries",empty_as_null=True)
        jobs_countries.table = "dbo.jobs_countries"
        jobs_skills = df_postings.select("job_id", "skills").explode("skills",empty_as_null=True)
        jobs_skills.table = "dbo.jobs_skills"
        jobs_cities = df_postings.select("job_id", "cities").explode("cities",empty_as_null=True) 
        jobs_cities.table = "dbo.jobs_cities"
        jobs_company_industries = df_postings.select("job_id","company_industries").explode("company_industries",empty_as_null=True)
        jobs_company_industries.table = "dbo.jobs_company_industries"
        jobs_company_types = df_postings.select("job_id", "company_types").explode("company_types",empty_as_null=True)
        jobs_company_types.table = "dbo.jobs_company_types"
        jobs_company_sizes = df_postings.select("job_id", "company_sizes").explode("company_sizes",empty_as_null=True)
        jobs_company_sizes.table = "dbo.jobs_company_sizes"
        jobs_company_domains = df_postings.select("job_id", "domains").explode("domains",empty_as_null=True)
        jobs_company_domains.table = "dbo.jobs_company_domains"
        
        list_df = [jobs_countries, jobs_skills, jobs_cities, jobs_company_industries,
                   jobs_company_types, jobs_company_sizes, jobs_company_domains]

        print(f"Loading {file.name}.")

        for df in list_df:

            print(f"Writing table {df.table} to DB")
            df.write_database(table_name=df.table, connection=sql_engine, if_table_exists="append")

        schema_complete = get_schema_jobs_pl()
        schema_no_list = get_schema_nolist(schema_complete)
        print("Writing jobs_posting table to DB")
        if file_nbr == 0:
            df_postings = pl.read_ndjson(file.path, schema=schema_no_list, row_index_name="job_id",ignore_errors=True)
            current_offset = df_postings.select("job_id").max().item() + 1
            file_nbr += 1
            print(f"Current offset: {current_offset}")
            df_postings.write_database(table_name="jobs_postings", connection=sql_engine, if_table_exists="append")

        else:
            df_postings = pl.read_ndjson(file.path, schema=schema_no_list,ignore_errors=True)
            df_postings = df_postings.with_row_index("job_id", offset=current_offset)
            current_offset = df_postings.select("job_id").max().item() + 1
            file_nbr += 1
            print(f"Current offset: {current_offset}")
            df_postings.write_database(table_name="jobs_postings", connection=sql_engine, if_table_exists="append")


if __name__ == "__main__" :
    load_to_bronze()
