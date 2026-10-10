# coding: utf-8
import polars as pl

import os

from utils.schema_override_survey import get_schema_survey_2025, get_schema_nolist_2025, get_schema_survey_22_24, get_schema_nolist_22_24

from utils.sql_server_utils import generate_conn_string, create_sqlserver_engine


def load_to_bronze():
    file_nbr = 0
    current_offset = 0
    conn_string = generate_conn_string("bronze_tfe")
    sql_engine = create_sqlserver_engine(conn_string)
    for file in os.scandir("/home/jm/projects/tfe/so_data_raw/answers/"):
        df_survey = pl.read_csv(file.path, row_index_name="answer_id")
        file_year = file.name[0:4]

        df_survey = df_survey.with_columns([pl.lit(file_year).alias("survey_year")])

        df_languages_worked = df_survey.with_columns(LanguageHaveWorkedWith = (df_survey.get_column("LanguageHaveWorkedWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year", "LanguageHaveWorkedWith").explode("LanguageHaveWorkedWith")
        df_languages_worked.table = "dbo.survey_programming_languages" 

        df_languages_want = df_survey.with_columns(LanguageWantToWorkWith
                                                   = (df_survey.get_column("LanguageWantToWorkWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year", "LanguageWantToWorkWith").explode("LanguageWantToWorkWith")       
        df_languages_want.table = "dbo.survey_programming_languages" 


        df_db_worked = df_survey.with_columns(DatabaseHaveWorkedWith = (df_survey.get_column("DatabaseHaveWorkedWith").explode().str.split(";"))).select("answer_id","ResponseId", "survey_year","DatabaseHaveWorkedWith").explode("DatabaseHaveWorkedWith")
        df_db_worked.table = "dbo.survey_databases"

        df_db_want = df_survey.with_columns(DatabaseWantToWorkWith = (df_survey.get_column("DatabaseWantToWorkWith").explode().str.split(";"))).select("answer_id","ResponseId", "survey_year","DatabaseWantToWorkWith").explode("DatabaseWantToWorkWith")
        df_db_want.table = "dbo.survey_databases"

        df_platform_worked = df_survey.with_columns(PlatformHaveWorkedWith = (df_survey.get_column("PlatformHaveWorkedWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year","PlatformHaveWorkedWith").explode("PlatformHaveWorkedWith")
        df_platform_worked.table = "dbo.survey_platforms"

        df_platform_want = df_survey.with_columns(PlatformWantToWorkWith = (df_survey.get_column("PlatformWantToWorkWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year","PlatformWantToWorkWith").explode("PlatformWantToWorkWith")
        df_platform_want.table = "dbo.survey_platforms"

        df_webframe_worked = df_survey.with_columns(WebframeHaveWorkedWith = (df_survey.get_column("WebframeHaveWorkedWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year","WebframeHaveWorkedWith").explode("WebframeHaveWorkedWith")
        df_webframe_worked.table = "dbo.survey_web_frameworks"

        df_webframe_want = df_survey.with_columns(WebframeWantToWorkWith = (df_survey.get_column("WebframeWantToWorkWith").explode().str.split(";"))).select("answer_id","ResponseId", "survey_year","WebframeWantToWorkWith").explode("WebframeWantToWorkWith")
        df_webframe_want.table = "dbo_survey_web_frameworks"

        if file_year == "2025":

            df_SOTag_worked = df_survey.with_columns(SOTagsHaveWorkedWith = (df_survey.get_column("SOTagsHaveWorkedWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year","SOTagsHaveWorkedWith").explode("SOTagsHaveWorkedWith")
            df_SOTag_worked.table = "dbo.survey_misc_techs"

            df_SOTags_want = df_survey.with_columns(SOTagsWantToWorkWith = (df_survey.get_column("SOTagsWantToWorkWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year","SOTagsWantToWorkWith").explode("SOTagsWantToWorkWith")
            df_SOTags_want.table = "dbo.survey_misc_techs"

            list_df = [df_languages_worked, df_languages_want, df_db_worked, df_db_want, df_platform_worked, df_platform_want, df_webframe_worked, df_webframe_want, df_SOTag_worked, df_SOTags_want]

            print(f"Loading {file.name}.")

            for df in list_df:

                print(f"Writing table {df.table} to DB")
                df.write_database(table_name=df.table, connection=sql_engine, if_table_exists="append")

            schema_complete = get_schema_survey_2025()
            schema_no_list = get_schema_nolist_2025(schema_complete)

            ##stopped
            print("Writing survey_answers table to DB")
            if file_nbr == 0:
                df_survey = pl.read_csv(file.path, row_index_name="answer_id")
                df_survey = df_survey.select(schema_no_list.keys())
                current_offset = df_survey.select("answer_id").max().item() + 1
                file_nbr += 1
                print(f"Current offset: {current_offset}")
                df_survey.write_database(table_name="dbo.survey_answers", connection=sql_engine, if_table_exists="append")

            else:
                df_survey = pl.read_csv(file.path)
                df_survey = df_survey.with_row_index("answer_id", offset=current_offset)
                df_survey = df_survey.select(schema_no_list.keys())
                current_offset = df_survey.select("answer_id").max().item() + 1
                file_nbr += 1
                print(f"Current offset: {current_offset}")
                df_survey.write_database(table_name="dbo.survey_answers", connection=sql_engine, if_table_exists="append")




        elif file_year != "2025":

            df_MiscTech_worked = df_survey.with_columns(MiscTechHaveWorkedWith = (df_survey.get_column("MiscTechHaveWorkedWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year","MiscTechHaveWorkedWith").explode("MiscTechHaveWorkedWith")
            df_MiscTech_worked.table = "dbo.survey_misc_techs"

            df_MiscTech_want = df_survey.with_columns(MiscTechWantToWorkWith = (df_survey.get_column("MiscTechWantToWorkWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year","MiscTechWantToWorkWith").explode("MiscTechWantToWorkWith")
            df_MiscTech_want.table = "dbo.survey_misc_techs"

            df_ToolsTech_worked = df_survey.with_columns(ToolsTechHaveWorkedWith = (df_survey.get_column("ToolsTechHaveWorkedWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year","ToolsTechHaveWorkedWith").explode("ToolsTechHaveWorkedWith")
            df_ToolsTech_worked.table = "dbo.survey_tools_tech"

            df_ToolsTech_want = df_survey.with_columns(ToolsTechWantToWorkWith = (df_survey.get_column("ToolsTechWantToWorkWith").explode().str.split(";"))).select("answer_id","ResponseId","survey_year","ToolsTechWantToWorkWith").explode("ToolsTechWantToWorkWith")
            df_ToolsTech_want.table = "dbo.survey_tools_tech"

            list_df = [df_languages_worked, df_languages_want, df_db_worked, df_db_want, df_platform_worked, df_platform_want, df_webframe_worked, df_webframe_want, df_MiscTech_worked, df_MiscTech_want, df_ToolsTech_worked, df_ToolsTech_want]


            print(f"Loading {file.name}.")

            for df in list_df:

                print(f"Writing table {df.table} to DB")
                df.write_database(table_name=df.table, connection=sql_engine, if_table_exists="append")

            schema_complete = get_schema_survey_22_24()
            schema_no_list = get_schema_nolist_22_24(schema_complete)

            print("Writing survey_answers table to DB")
            if file_nbr == 0:
                df_survey = pl.read_csv(file.path, row_index_name="answer_id")
                df_survey = df_survey.select(schema_no_list.keys())
                current_offset = df_survey.select("answer_id").max().item() + 1
                file_nbr += 1
                print(f"Current offset: {current_offset}")
                df_survey.write_database(table_name="dbo.survey_answers", connection=sql_engine, if_table_exists="append")

            else:
                df_survey = pl.read_csv(file.path)
                df_survey = df_survey.with_row_index("answer_id", offset=current_offset)
                df_survey = df_survey.select(schema_no_list.keys())
                current_offset = df_survey.select("answer_id").max().item() + 1
                file_nbr += 1
                print(f"Current offset: {current_offset}")
                df_survey.write_database(table_name="dbo.survey_answers", connection=sql_engine, if_table_exists="append")



if __name__ == "__main__" :
    load_to_bronze()
