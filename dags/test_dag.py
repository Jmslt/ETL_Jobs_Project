from airflow.sdk import task, dag
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

import os

from utils.jsonl_utils import validateJSONL, cleanJSONL


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

sql1 = SQLExecuteQueryOperator(
    task_id="create_bronze_db",
    conn_id= "mssql_default",
    sql="sql/create_db_bronze.sql",
    autocommit=True
    )

@dag(
    dag_id = "TFE_pipeline",
    tags=["tfe"]
)
def generate_dag():
    task1 = validate_jsonl_files()
    task2 = clean_jsonl_files()
    task3 = sql1

    task1 >> task2 >> task3


generate_dag()
