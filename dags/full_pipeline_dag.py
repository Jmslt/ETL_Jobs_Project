from airflow.sdk import task, dag, DAG, Param
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


with DAG(
    dag_id="1_TFE_full_pipeline"
) as dag:
    download_jobs_data = TriggerDagRunOperator(
        task_id="download_jobs_data",
        trigger_dag_id="TFE_download_jobs_data",
        wait_for_completion=True,
        poke_interval=30)

    download_survey_data = TriggerDagRunOperator(
        task_id="download_survey_data",
        trigger_dag_id="TFE_download_survey_data",
        wait_for_completion=True,
        poke_interval=30)

    load_bronze_data = TriggerDagRunOperator(
        task_id="load_bronze_data",
        trigger_dag_id="TFE_load_bronze",
        wait_for_completion=True,
        poke_interval=30)

    load_silver_data = TriggerDagRunOperator(
        task_id="load_silver_data",
        trigger_dag_id="TFE_load_silver",
        wait_for_completion=True,
        poke_interval=30)

    load_gold_data = TriggerDagRunOperator(
        task_id="load_gold_data",
        trigger_dag_id="TFE_load_gold",
        wait_for_completion=True,
        poke_interval=30)

    [download_jobs_data, download_survey_data] >> load_bronze_data >> load_silver_data >> load_gold_data
