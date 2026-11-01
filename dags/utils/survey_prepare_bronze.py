'''
This utility script contains the functions needed to cleand and load
the survey data to the Bronze layer on our DB.
'''
import polars as pl

import os

from utils.schema_override_survey import get_schema_survey_2025, get_schema_nolist_2025, get_schema_survey_22_24, get_schema_nolist_22_24

from utils.sql_server_utils import generate_conn_string, create_sqlserver_engine

LIST_COLUMNS = {
    "language":["LanguageHaveWorkedWith", "LanguageWantToWorkWith"],
    "database":["DatabaseHaveWorkedWith","DatabaseWantToWorkWith"],
    "platform":["PlatformHaveWorkedWith", "PlatformWantToWorkWith"],
    "web_framework":["WebframeHaveWorkedWith", "WebframeWantToWorkWith"],
    "misc_tech":["MiscTechHaveWorkedWith", "MiscTechWantToWorkWith"],
    "tool_tech":["ToolsTechHaveWorkedWith", "ToolsTechWantToWorkWith"],
}

LIST_COLUMNS_2025 = {
    "language":["LanguageHaveWorkedWith", "LanguageWantToWorkWith"],
    "database":["DatabaseHaveWorkedWith","DatabaseWantToWorkWith"],
    "platform":["PlatformHaveWorkedWith", "PlatformWantToWorkWith"],
    "web_framework":["WebframeHaveWorkedWith", "WebframeWantToWorkWith"],
    "misc_tech":["SOTagsHaveWorkedWith", "SOTagsWantToWorkWith"]
}


LIST_TABLES = {
    "language": "dbo.survey_programming_languages",
    "database": "dbo.survey_databases",
    "platform": "dbo.survey_platforms",
    "web_framework": "dbo.survey_web_frameworks",
    "misc_tech": "dbo.survey_misc_techs",
    "tool_tech": "dbo.survey_tools_tech",
    "sotag": "dbo.survey_misc_techs"
}


def create_answers_df(file, offset):
    '''
    Creates a Polars Dataframe with all answers from the survey
    '''
    df_survey = pl.read_csv(file.path, row_index_name="answer_id", row_index_offset=offset, ignore_errors=True)
    file_year = file.name[0:4]
    df_survey = df_survey.with_columns([pl.lit(file_year).alias("survey_year")])
    df_survey = df_survey.with_columns(pl.col(pl.String).replace("NA", None))
    return df_survey


def create_skills_df(df, file):
    '''
    Creates a Polars Dataframe for each types of skill considered by the
    surveys.
    For the 2025 survey, the category "SOTag" is equivalent to misc_techs.
    '''
    dict_skills_tables = {}
    if file.name[0:4] == "2025":
        for table, column in LIST_COLUMNS_2025.items():
            dict_skills_tables[column[0]] = df.with_columns(pl.col(column[0]).explode(empty_as_null=True).str.split(";")).select("answer_id","ResponseId","survey_year",column[0]).explode(column[0],empty_as_null=True)

            dict_skills_tables[column[0]] = dict_skills_tables[column[0]].rename({column[0]:table})
            dict_skills_tables[column[0]] = dict_skills_tables[column[0]].with_columns([pl.lit("True").alias("worked_with")])
            dict_skills_tables[column[0]] = dict_skills_tables[column[0]].with_columns([pl.lit("NA").alias("want_to_work_with")])
            dict_skills_tables[column[0]] = dict_skills_tables[column[0]].with_columns(pl.col(pl.String).replace("NA", None))
            dict_skills_tables[column[0]].table = LIST_TABLES.get(table)

            dict_skills_tables[column[1]] = df.with_columns(pl.col(column[1]).explode(empty_as_null=True).str.split(";")).select("answer_id","ResponseId","survey_year",column[1]).explode(column[1],empty_as_null=True)
            dict_skills_tables[column[1]] = dict_skills_tables[column[1]].rename({column[1]:table})
            dict_skills_tables[column[1]] = dict_skills_tables[column[1]].with_columns([pl.lit("NA").alias("worked_with")])
            dict_skills_tables[column[1]] = dict_skills_tables[column[1]].with_columns([pl.lit("True").alias("want_to_work_with")])
            dict_skills_tables[column[1]] = dict_skills_tables[column[1]].with_columns(pl.col(pl.String).replace("NA", None))
            dict_skills_tables[column[1]].table = LIST_TABLES.get(table)

    else:
        for table, column in LIST_COLUMNS.items():
            dict_skills_tables[column[0]] = df.with_columns(pl.col(column[0]).explode(empty_as_null=True).str.split(";")).select("answer_id","ResponseId","survey_year",column[0]).explode(column[0],empty_as_null=True)

            dict_skills_tables[column[0]] = dict_skills_tables[column[0]].rename({column[0]:table})
            dict_skills_tables[column[0]] = dict_skills_tables[column[0]].with_columns([pl.lit("True").alias("worked_with")])
            dict_skills_tables[column[0]] = dict_skills_tables[column[0]].with_columns([pl.lit("NA").alias("want_to_work_with")])
            dict_skills_tables[column[0]] = dict_skills_tables[column[0]].with_columns(pl.col(pl.String).replace("NA", None))
            dict_skills_tables[column[0]].table = LIST_TABLES.get(table)

            dict_skills_tables[column[1]] = df.with_columns(pl.col(column[1]).explode(empty_as_null=True).str.split(";")).select("answer_id","ResponseId","survey_year",column[1]).explode(column[1],empty_as_null=True)
            dict_skills_tables[column[1]] = dict_skills_tables[column[1]].rename({column[1]:table})
            dict_skills_tables[column[1]] = dict_skills_tables[column[1]].with_columns([pl.lit("NA").alias("worked_with")])
            dict_skills_tables[column[1]] = dict_skills_tables[column[1]].with_columns([pl.lit("True").alias("want_to_work_with")])
            dict_skills_tables[column[1]] = dict_skills_tables[column[1]].with_columns(pl.col(pl.String).replace("NA", None))
            dict_skills_tables[column[1]].table = LIST_TABLES.get(table)
    return dict_skills_tables


def load_skills_to_db(dict_df, fast_param):
    '''
    Takes the Dataframes from the dictionnary and loads them
    into the Bronze layer of our DB.
    '''
    conn_string = generate_conn_string("bronze_tfe")
    sql_engine = create_sqlserver_engine(conn_string, fast=fast_param)
    for df_name, df in dict_df.items():
        print(f"Writing table {df.table} to DB")
        df.write_database(table_name=df.table, connection=sql_engine, if_table_exists="append")



def load_answers_to_db(file, fast_param, offset):
    '''
    Creates a new amswers Dataframe, assigns it the correct
    Index using a manually created offset, and loads it to
    the Bronze layer of our DB.
    The 2025 survey has a different number of columns, so we use
    a different schema.
    '''
    conn_string = generate_conn_string("bronze_tfe")
    sql_engine = create_sqlserver_engine(conn_string, fast=fast_param)
    if file.name[0:4] == "2025":
        schema_complete = get_schema_survey_2025()
        schema_no_list = get_schema_nolist_2025(schema_complete)
        print("Writing answers table to DB")
        df_answers = pl.read_csv(file.path, schema=schema_no_list, extra_columns="ignore", row_index_offset= offset, row_index_name="answer_id",ignore_errors=True, missing_columns="insert")
        file_year = file.name[0:4]
        df_answers = df_answers.with_columns([pl.lit(file_year).alias("survey_year")])
        df_answers = df_answers.with_columns(pl.col(pl.String).replace("NA", None))
        new_offset = df_answers.select("answer_id").max().item() + 1
        print(f"Current offset: {new_offset}")
        df_answers.write_database(table_name="dbo.survey_answers", connection=sql_engine, if_table_exists="append")
        return new_offset

    else:
        schema_complete = get_schema_survey_22_24()
        schema_no_list = get_schema_nolist_22_24(schema_complete)
        print("Writing answers table to DB")
        df_answers = pl.read_csv(file.path, schema=schema_no_list, extra_columns="ignore", row_index_offset= offset, row_index_name="answer_id",ignore_errors=True, missing_columns="insert")
        file_year = file.name[0:4]
        df_answers = df_answers.with_columns([pl.lit(file_year).alias("survey_year")])
        df_answers = df_answers.with_columns(pl.col(pl.String).replace("NA", None))
        new_offset = df_answers.select("answer_id").max().item() + 1
        print(f"Current offset: {new_offset}")
        df_answers.write_database(table_name="dbo.survey_answers", connection=sql_engine, if_table_exists="append")
        return new_offset


def load_survey_to_bronze(fast_param):
    '''
    This function orchestrates the whole process.
    This is the function called by the Airflow DAG.
    '''
    current_offset = 0

    for file in os.scandir("data/survey/"):
        print(f"Current file being loaded: {file.name}")
        answers_df = create_answers_df(file, current_offset)
        dict_skills_tables = create_skills_df(answers_df, file)
        load_skills_to_db(dict_skills_tables, fast_param)
        current_offset = load_answers_to_db(file, fast_param, current_offset)
