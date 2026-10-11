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
        df_survey = pl.DataFrame()
        if file_nbr == 0:
            df_survey = pl.read_csv(file.path, row_index_name="answer_id")
            file_year = file.name[0:4]
            df_survey = df_survey.with_columns([pl.lit(file_year).alias("survey_year")])

        else:
            df_survey = pl.read_csv(file.path)
            file_year = file.name[0:4]
            df_survey = df_survey.with_row_index("answer_id", offset=current_offset)
            df_survey = df_survey.with_columns([pl.lit(file_year).alias("survey_year")])





        df_languages_worked = df_survey.with_columns(LanguageHaveWorkedWith = (df_survey.get_column("LanguageHaveWorkedWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","LanguageHaveWorkedWith").explode("LanguageHaveWorkedWith",empty_as_null=True)
        df_languages_worked = df_languages_worked.rename({"LanguageHaveWorkedWith": "language"})
        df_languages_worked = df_languages_worked.with_columns([pl.lit("True").alias("worked_with")])
        df_languages_worked = df_languages_worked.with_columns([pl.lit("NA").alias("want_to_work_with")])
        df_languages_worked.table = "dbo.survey_programming_languages"

        df_languages_want = df_survey.with_columns(LanguageWantToWorkWith = (df_survey.get_column("LanguageWantToWorkWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","LanguageWantToWorkWith").explode("LanguageWantToWorkWith",empty_as_null=True)
        df_languages_want = df_languages_want.rename({"LanguageWantToWorkWith": "language"})
        df_languages_want = df_languages_want.with_columns([pl.lit("NA").alias("worked_with")])
        df_languages_want = df_languages_want.with_columns([pl.lit("True").alias("want_to_work_with")])
        df_languages_want.table = "dbo.survey_programming_languages" 


        df_db_worked = df_survey.with_columns(DatabaseHaveWorkedWith = (df_survey.get_column("DatabaseHaveWorkedWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId", "survey_year","DatabaseHaveWorkedWith").explode("DatabaseHaveWorkedWith",empty_as_null=True)
        df_db_worked = df_db_worked.rename({"DatabaseHaveWorkedWith": "database"})
        df_db_worked = df_db_worked.with_columns([pl.lit("True").alias("worked_with")])
        df_db_worked = df_db_worked.with_columns([pl.lit("NA").alias("want_to_work_with")])
        df_db_worked.table = "dbo.survey_databases"

        df_db_want = df_survey.with_columns(DatabaseWantToWorkWith = (df_survey.get_column("DatabaseWantToWorkWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","DatabaseWantToWorkWith").explode("DatabaseWantToWorkWith",empty_as_null=True)
        df_db_want = df_db_want.rename({"DatabaseWantToWorkWith": "database"})
        df_db_want = df_db_want.with_columns([pl.lit("NA").alias("worked_with")])
        df_db_want = df_db_want.with_columns([pl.lit("True").alias("want_to_work_with")])
        df_db_want.table = "dbo.survey_databases"

        df_platform_worked = df_survey.with_columns(PlatformHaveWorkedWith = (df_survey.get_column("PlatformHaveWorkedWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","PlatformHaveWorkedWith").explode("PlatformHaveWorkedWith",empty_as_null=True)
        df_platform_worked = df_platform_worked.rename({"PlatformHaveWorkedWith": "platform"})
        df_platform_worked = df_platform_worked.with_columns([pl.lit("True").alias("worked_with")])
        df_platform_worked = df_platform_worked.with_columns([pl.lit("NA").alias("want_to_work_with")])
        df_platform_worked.table = "dbo.survey_platforms"

        df_platform_want = df_survey.with_columns(PlatformWantToWorkWith = (df_survey.get_column("PlatformWantToWorkWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","PlatformWantToWorkWith").explode("PlatformWantToWorkWith", empty_as_null=True)
        df_platform_want = df_platform_want.rename({"PlatformWantToWorkWith": "platform"})
        df_platform_want = df_platform_want.with_columns([pl.lit("NA").alias("worked_with")])
        df_platform_want = df_platform_want.with_columns([pl.lit("True").alias("want_to_work_with")])
        df_platform_want.table = "dbo.survey_platforms"

        df_webframe_worked = df_survey.with_columns(WebframeHaveWorkedWith = (df_survey.get_column("WebframeHaveWorkedWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","WebframeHaveWorkedWith").explode("WebframeHaveWorkedWith",empty_as_null=True)
        df_webframe_worked = df_webframe_worked.rename({"WebframeHaveWorkedWith": "web_framework"})
        df_webframe_worked = df_webframe_worked.with_columns([pl.lit("True").alias("worked_with")])
        df_webframe_worked = df_webframe_worked.with_columns([pl.lit("NA").alias("want_to_work_with")])
        df_webframe_worked.table = "dbo.survey_web_frameworks"

        df_webframe_want = df_survey.with_columns(WebframeWantToWorkWith = (df_survey.get_column("WebframeWantToWorkWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId", "survey_year","WebframeWantToWorkWith").explode("WebframeWantToWorkWith",empty_as_null=True)
        df_webframe_want = df_webframe_want.rename({"WebframeWantToWorkWith": "web_framework"})
        df_webframe_want = df_webframe_want.with_columns([pl.lit("NA").alias("worked_with")])
        df_webframe_want = df_webframe_want.with_columns([pl.lit("True").alias("want_to_work_with")])
        df_webframe_want.table = "dbo.survey_web_frameworks"

        if file_year == "2025":

            df_SOTag_worked = df_survey.with_columns(SOTagsHaveWorkedWith = (df_survey.get_column("SOTagsHaveWorkedWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","SOTagsHaveWorkedWith").explode("SOTagsHaveWorkedWith",empty_as_null=True)
            df_SOTag_worked = df_SOTag_worked.rename({"SOTagsHaveWorkedWith": "misc_tech"})
            df_SOTag_worked = df_SOTag_worked.with_columns([pl.lit("True").alias("worked_with")])
            df_SOTag_worked = df_SOTag_worked.with_columns([pl.lit("NA").alias("want_to_work_with")])
            df_SOTag_worked.table = "dbo.survey_misc_techs"

            df_SOTags_want = df_survey.with_columns(SOTagsWantToWorkWith = (df_survey.get_column("SOTagsWantToWorkWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","SOTagsWantToWorkWith").explode("SOTagsWantToWorkWith",empty_as_null=True)
            df_SOTags_want = df_SOTags_want.rename({"SOTagsWantToWorkWith": "misc_tech"})
            df_SOTags_want = df_SOTags_want.with_columns([pl.lit("NA").alias("worked_with")])
            df_SOTags_want = df_SOTags_want.with_columns([pl.lit("True").alias("want_to_work_with")])
            df_SOTags_want.table = "dbo.survey_misc_techs"

            list_df = [df_languages_worked, df_languages_want, df_db_worked, df_db_want, df_platform_worked, df_platform_want, df_webframe_worked, df_webframe_want, df_SOTag_worked, df_SOTags_want]

            print(f"Loading {file.name}.")

            for df in list_df:

                print(f"Writing table {df.table} to DB")
                df.write_database(table_name=df.table, connection=sql_engine, if_table_exists="append")

            schema_complete = get_schema_survey_2025()
            schema_no_list = get_schema_nolist_2025(schema_complete)

            
            print("Writing survey_answers table to DB")
            if file_nbr == 0:
                df_survey = pl.read_csv(file.path, row_index_name="answer_id")
                df_survey = df_survey.with_columns([pl.lit(file_year).alias("survey_year")])
                df_survey = df_survey.select(schema_no_list.keys())
                current_offset = df_survey.select("answer_id").max().item() + 1
                file_nbr += 1
                print(f"Current offset: {current_offset}")
                df_survey.write_database(table_name="dbo.survey_answers", connection=sql_engine, if_table_exists="append")

            else:
                df_survey = pl.read_csv(file.path)
                df_survey = df_survey.with_row_index("answer_id", offset=current_offset)
                df_survey = df_survey.with_columns([pl.lit(file_year).alias("survey_year")])
                df_survey = df_survey.select(schema_no_list.keys())
                current_offset = df_survey.select("answer_id").max().item() + 1
                file_nbr += 1
                print(f"Current offset: {current_offset}")
                df_survey.write_database(table_name="dbo.survey_answers", connection=sql_engine, if_table_exists="append")




        elif file_year != "2025":

            df_MiscTech_worked = df_survey.with_columns(MiscTechHaveWorkedWith = (df_survey.get_column("MiscTechHaveWorkedWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","MiscTechHaveWorkedWith").explode("MiscTechHaveWorkedWith",empty_as_null=True)
            df_MiscTech_worked = df_MiscTech_worked.rename({"MiscTechHaveWorkedWith": "misc_tech"})
            df_MiscTech_worked = df_MiscTech_worked.with_columns([pl.lit("True").alias("worked_with")])
            df_MiscTech_worked = df_MiscTech_worked.with_columns([pl.lit("NA").alias("want_to_work_with")])
            df_MiscTech_worked.table = "dbo.survey_misc_techs"

            df_MiscTech_want = df_survey.with_columns(MiscTechWantToWorkWith = (df_survey.get_column("MiscTechWantToWorkWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","MiscTechWantToWorkWith").explode("MiscTechWantToWorkWith",empty_as_null=True)
            df_MiscTech_want = df_MiscTech_want.rename({"MiscTechWantToWorkWith": "misc_tech"})
            df_MiscTech_want = df_MiscTech_want.with_columns([pl.lit("NA").alias("worked_with")])
            df_MiscTech_want = df_MiscTech_want.with_columns([pl.lit("True").alias("want_to_work_with")])
            df_MiscTech_want.table = "dbo.survey_misc_techs"

            df_ToolsTech_worked = df_survey.with_columns(ToolsTechHaveWorkedWith = (df_survey.get_column("ToolsTechHaveWorkedWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","ToolsTechHaveWorkedWith").explode("ToolsTechHaveWorkedWith",empty_as_null=True)
            df_ToolsTech_worked = df_ToolsTech_worked.rename({"ToolsTechHaveWorkedWith": "tool_tech"})
            df_ToolsTech_worked = df_ToolsTech_worked.with_columns([pl.lit("True").alias("worked_with")])
            df_ToolsTech_worked = df_ToolsTech_worked.with_columns([pl.lit("NA").alias("want_to_work_with")])
            df_ToolsTech_worked.table = "dbo.survey_tools_tech"

            df_ToolsTech_want = df_survey.with_columns(ToolsTechWantToWorkWith = (df_survey.get_column("ToolsTechWantToWorkWith").explode(empty_as_null=True).str.split(";"))).select("answer_id","ResponseId","survey_year","ToolsTechWantToWorkWith").explode("ToolsTechWantToWorkWith",empty_as_null=True)
            df_ToolsTech_want = df_ToolsTech_want.rename({"ToolsTechWantToWorkWith": "tool_tech"})
            df_ToolsTech_want = df_ToolsTech_want.with_columns([pl.lit("NA").alias("worked_with")])
            df_ToolsTech_want = df_ToolsTech_want.with_columns([pl.lit("True").alias("want_to_work_with")])
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
                df_survey = df_survey.with_columns([pl.lit(file_year).alias("survey_year")])
                df_survey = df_survey.select(schema_no_list.keys())
                current_offset = df_survey.select("answer_id").max().item() + 1
                file_nbr += 1
                print(f"Current offset: {current_offset}")
                df_survey.write_database(table_name="dbo.survey_answers", connection=sql_engine, if_table_exists="append")

            else:
                df_survey = pl.read_csv(file.path)
                df_survey = df_survey.with_row_index("answer_id", offset=current_offset)
                df_survey = df_survey.with_columns([pl.lit(file_year).alias("survey_year")])
                df_survey = df_survey.select(schema_no_list.keys())
                current_offset = df_survey.select("answer_id").max().item() + 1
                file_nbr += 1
                print(f"Current offset: {current_offset}")
                df_survey.write_database(table_name="dbo.survey_answers", connection=sql_engine, if_table_exists="append")



if __name__ == "__main__" :
    load_to_bronze()
