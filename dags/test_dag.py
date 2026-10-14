from airflow.sdk import task, dag
import os

from utils.jsonl_utils import validateJSONL

@task(task_id = "validate_jsonl_files")
def validate_jsonl_files():
    for file in os.scandir("data/jobs/"):
        if file.is_file():
            print("file: " + file.name)
            validateJSONL(file, 3)


@dag(
    dag_id = "TFE_pipeline",
    tags=["tfe"]
)
def generate_dag():
    task1 = validate_jsonl_files()

    task1

generate_dag()
