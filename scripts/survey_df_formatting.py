# coding: utf-8
import polars as pl

import os

from utils.schema_override_survey import get_schema_survey_2025, get_schema_nolist_2025, get_schema_survey_22_24, get_schema_nolist_22_24

from utils.sql_server_utils import generate_conn_string, create_sqlserver_engine

conn_string = generate_conn_string("bronze_tfe")
sql_engine = create_sqlserver_engine(conn_string)
conn_string = generate_conn_string("bronze_tfe")
sql_engine = create_sqlserver_engine(conn_string)
df_survey = pl.read_csv("/home/jm/projects/tfe/so_data_raw/answers/2025.csv", row_index_name="answer_id")
df_survey = df_survey.with_columns([pl.lit("2025").alias("Year")])
df_languages_worked = df_survey.with_columns(LanguageHaveWorkedWith = (df_survey.get_column("LanguageHaveWorkedWith").explode().str.split(";"))).select("answer_id","ResponseId","Year", "LanguageHaveWorkedWith").explode("LanguageHaveWorkedWith")


df_languages_want = df_survey.with_columns(LanguageWantToWorkWith = (df_survey.get_column("LanguageWantToWorkWith").explode().str.split(";"))).select("answer_id","ResponseId","Year", "LanguageWantToWorkWith").explode("LanguageWantToWorkWith")       


df_languages_worked = df_languages_worked.rename({"LanguageHaveWorkedWith": "language"})
df_languages_want = df_languages_want.rename({"LanguageWantToWorkWith": "language"})

df_languages_worked = df_languages_worked.with_columns([pl.lit("True").alias("worked_with")])
df_languages_worked = df_languages_worked.with_columns([pl.lit("False").alias("want_to_work_with")])

df_languages_want = df_languages_want.with_columns([pl.lit("False").alias("worked_with")])
df_languages_want = df_languages_want.with_columns([pl.lit("True").alias("want_to_work_with")])

df_languages_worked.table = "dbo.survey_programming_languages"
df_languages_want.table = "dbo.survey_programming_languages"

list_df = [df_languages_worked, df_languages_want]

for df in list_df:
    print(f"Writing table {df.table} to DB")
    df.write_database(table_name=df.table, connection=sql_engine, if_table_exists="append")
