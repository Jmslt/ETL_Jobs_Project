from airflow.sdk import task, dag
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

import os

from utils.jsonl_utils import validateJSONL, cleanJSONL
from utils.sql_server_utils import generate_conn_string


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

@task(task_id="create_bronze_db")
def create_bronze_db():
    sql1 = SQLExecuteQueryOperator(
        task_id="create_bronze_db",
        conn_id= mssql.MsSqlHook.get_conn(generate_conn_string("master")),
        sql=r"CREATE DATABASE testdb;",
        autocommit=True
    )

@dag(
    dag_id = "TFE_pipeline",
    tags=["tfe"]
)
def generate_dag():
    task1 = validate_jsonl_files()
    task2 = clean_jsonl_files()
    task3 = create_bronze_db()

#    task1 >> task2 >> task3
    task3
generate_dag()
