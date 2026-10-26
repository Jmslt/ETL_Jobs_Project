from airflow.sdk import task, dag, DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


from utils.download_survey_data_util import download_survey_csv


@task(task_id = "download_survey_data")
def download_survey_data():
    download_survey_csv()


@dag(
    dag_id = "TFE_download_survey_data",
    tags=["tfe", "download", "survey"]
)
def generate_dag():
    task1 = download_survey_data()

    task1

generate_dag()
