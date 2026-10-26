from airflow.sdk import task, dag, DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


from utils.download_jobs_data_util import download_archives_huggingface, unzip_archives_jobs, delete_archives_huggingface



@task(task_id = "download_huggingface_archives")
def download_huggingface_archives():
    download_archives_huggingface()

@task(task_id = "unzip_huggingface_archives")
def unzip_huggingface_archives():
    unzip_archives_jobs()

@task(task_id = "delete_huggingface_archives")
def delete_huggingface_archives():
    delete_archives_huggingface()


@dag(
    dag_id = "TFE_download_jobs_data",
    tags=["tfe", "download", "jobs"]
)
def generate_dag():
    task1 = download_huggingface_archives()
    task2 = unzip_huggingface_archives()
    task3 = delete_huggingface_archives()

    task1 >> task2 >> task3

generate_dag()
