from airflow.sdk import task, dag, DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

import os

from utils.jsonl_utils import validateJSONL, cleanJSONL
from utils.schema_override_jobs import get_schema_jobs_pl, get_schema_nolist, list_columns_complete
from utils.jobs_prepare_bronze import load_jobs_to_bronze

from utils.survey_prepare_bronze import load_survey_to_bronze
from utils.schema_override_survey import get_schema_survey_2025, get_schema_nolist_2025, get_schema_survey_22_24, get_schema_nolist_22_24


@task(task_id = "validate_jsonl_files")
def validate_jsonl_files():
    for file in os.scandir("data/jobs/"):
        if file.is_file():
            print("file: " + file.name)
            validateJSONL(file, 3)

@task(task_id = "clean_jsonl_files")
def clean_jsonl_files():
    for file in os.scandir("data/jobs/"):
        if file.is_file():
            print("Cleaning file: " + file.name)
            cleanJSONL(file)
    print("Cleaning over.")

sql_create_db_bronze = SQLExecuteQueryOperator(
    task_id="create_bronze_db",
    conn_id= "mssql_default",
    sql="sql/bronze/create_db_bronze.sql",
    autocommit=True
    )

sql_create_tables_jobs_bronze = SQLExecuteQueryOperator(
    task_id="sql_create_tables_jobs_bronze",
    conn_id="mssql_default",
    sql="sql/bronze/create_tables_jobs_BRONZE.sql",
    autocommit=True
)

@task(task_id="transform_and_load_jobs_bronze")
def transform_and_load_jobs_bronze():
    load_jobs_to_bronze()

sql_create_tables_survey_bronze = SQLExecuteQueryOperator(
    task_id="sql_create_tables_survey_bronze",
    conn_id="mssql_default",
    sql="sql/bronze/create_tables_survey_BRONZE.sql",
    autocommit=True
)

@task(task_id="transform_and_load_survey_bronze")
def transform_and_load_survey_bronze():
    load_survey_to_bronze()


@dag(
    dag_id = "TFE_load_bronze",
    tags=["tfe", "bronze"]
)
def generate_dag():
    task1 = validate_jsonl_files()
    task2 = clean_jsonl_files()
    task3 = sql_create_db_bronze
    task4 = sql_create_tables_jobs_bronze
    task5 = transform_and_load_jobs_bronze()
    task6 = sql_create_tables_survey_bronze
    task7 = transform_and_load_survey_bronze()

    task1 >> task2 >> task3 >> task4 >> task5 >> task6 >> task7

generate_dag()
