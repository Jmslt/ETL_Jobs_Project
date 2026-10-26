from airflow.sdk import task, dag, DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

with DAG(
    dag_id="TFE_load_silver",
    tags=["tfe", "silver"]
) as dag:
    sql_create_db_silver = SQLExecuteQueryOperator(
        task_id="sql_create_db_silver",
        conn_id="mssql_default",
        sql="sql/silver/create_db_SILVER.sql",
        autocommit=True
)

    sql_create_tables_jobs_silver = SQLExecuteQueryOperator(
        task_id="sql_create_tables_jobs_silver",
        conn_id="mssql_silver",
        sql="sql/silver/create_tables_jobs_SILVER.sql",
        autocommit=True
)

    sql_create_tables_survey_silver = SQLExecuteQueryOperator(
        task_id="sql_create_tables_survey_silver",
        conn_id="mssql_silver",
        sql="sql/silver/create_tables_survey_SILVER.sql",
        autocommit=True
)

# In order to change the VARCHAR salaries into INT,
# we need to delete the unrealistic values (ex: 9999999e36)
    sql_clean_unrealistic_salaries = SQLExecuteQueryOperator(
        task_id="sql_clean_unrealistic_salaries",
        conn_id="mssql_default",
        sql="sql/silver/clean_salaries_SURVEY_SILVER.sql",
        autocommit=True
)


    sql_create_views_jobs_silver = SQLExecuteQueryOperator(
        task_id="sql_create_views_jobs_silver",
        conn_id="mssql_silver",
        sql="sql/silver/create_views_jobs_SILVER.sql",
        split_statements=True,
        autocommit=True
)


    sql_create_views_survey_silver = SQLExecuteQueryOperator(
        task_id="sql_create_views_survey_silver",
        conn_id="mssql_silver",
        sql="sql/silver/create_views_survey_SILVER.sql",
        split_statements=True,
        autocommit=True
)


    sql_load_data_jobs_silver = SQLExecuteQueryOperator(
        task_id="sql_load_data_jobs_silver",
        conn_id="mssql_silver",
        sql="sql/silver/load_data_jobs_SILVER.sql",
        autocommit=True
)


    sql_load_data_survey_silver = SQLExecuteQueryOperator(
        task_id="sql_load_data_survey_silver",
        conn_id="mssql_silver",
        sql="sql/silver/load_data_survey_SILVER.sql",
        autocommit=True
)

    task1 = sql_create_db_silver
    task2 = sql_create_tables_jobs_silver
    task3 = sql_create_tables_survey_silver
    task4 = sql_clean_unrealistic_salaries
    task5 = sql_create_views_jobs_silver
    task6 = sql_create_views_survey_silver
    task7 = sql_load_data_jobs_silver
    task8 = sql_load_data_survey_silver

    task1 >> task2 >> task3 >> task4 >> task5 >> task6 >> task7 >> task8
