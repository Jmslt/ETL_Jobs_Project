from airflow.sdk import task, dag, DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

with DAG(
    dag_id="TFE_load_gold",
    tags=["tfe", "gold"]    
) as dag:
    sql_create_db_gold = SQLExecuteQueryOperator(
        task_id="sql_create_db_gold",
        conn_id="mssql_default",
        sql="sql/gold/create_db_GOLD.sql",
        autocommit=True
)

#JOBS

    sql_create_dims_jobs_gold = SQLExecuteQueryOperator(
        task_id="sql_create_dims_jobs_gold",
        conn_id="mssql_gold",
        sql="sql/gold/create_dims_jobs_GOLD.sql",
        autocommit=True
)


    sql_create_facts_jobs_gold = SQLExecuteQueryOperator(
        task_id="sql_create_facts_jobs_gold",
        conn_id="mssql_gold",
        sql="sql/gold/create_facts_jobs_GOLD.sql",
        autocommit=True
)


    sql_create_br_jobs_gold = SQLExecuteQueryOperator(
        task_id="sql_create_br_jobs_gold",
        conn_id="mssql_gold",
        sql="sql/gold/create_BR_jobs_GOLD.sql",
        autocommit=True
)

    sql_create_views_jobs_gold = SQLExecuteQueryOperator(
        task_id="sql_create_views_jobs_gold",
        conn_id="mssql_gold",
        sql="sql/gold/create_views_jobs_GOLD.sql",
        split_statements=True,
        autocommit=True
)

    sql_load_dims_jobs_gold = SQLExecuteQueryOperator(
        task_id="sql_load_dims_jobs_gold",
        conn_id="mssql_gold",
        sql="sql/gold/load_data_jobs_dim_GOLD.sql",
        autocommit=True
)

    sql_load_facts_jobs_gold = SQLExecuteQueryOperator(
        task_id="sql_load_facts_jobs_gold",
        conn_id="mssql_gold",
        sql="sql/gold/load_data_jobs_facts_GOLD.sql",
        autocommit=True
)

    sql_load_br_jobs_gold = SQLExecuteQueryOperator(
        task_id="sql_load_br_jobs_gold",
        conn_id="mssql_gold",
        sql="sql/gold/load_data_jobs_BR_GOLD.sql",
        autocommit=True
)

#SURVEY

    sql_create_dims_survey_gold = SQLExecuteQueryOperator(
        task_id="sql_create_dims_survey_gold",
        conn_id="mssql_gold",
        sql="sql/gold/create_dims_survey_GOLD.sql",
        autocommit=True
)

    sql_create_facts_survey_gold = SQLExecuteQueryOperator(
        task_id="sql_create_facts_survey_gold",
        conn_id="mssql_gold",
        sql="sql/gold/create_facts_survey_GOLD.sql",
        autocommit=True
)

    sql_create_br_survey_gold = SQLExecuteQueryOperator(
        task_id="sql_create_br_survey_gold",
        conn_id="mssql_gold",
        sql="sql/gold/create_BR_survey_GOLD.sql",
        autocommit=True
)

    sql_create_views_survey_gold = SQLExecuteQueryOperator(
        task_id="sql_create_views_survey_gold",
        conn_id="mssql_gold",
        sql="sql/gold/create_views_survey_GOLD.sql",
        split_statements=True,
        autocommit=True
)

    sql_load_dims_survey_gold = SQLExecuteQueryOperator(
        task_id="sql_load_dims_survey_gold",
        conn_id="mssql_gold",
        sql="sql/gold/load_data_survey_dim_GOLD.sql",
        autocommit=True
)

    sql_load_facts_survey_gold = SQLExecuteQueryOperator(
        task_id="sql_load_facts_survey_gold",
        conn_id="mssql_gold",
        sql="sql/gold/load_data_survey_facts_GOLD.sql",
        autocommit=True
)

    sql_load_br_survey_gold = SQLExecuteQueryOperator(
        task_id="sql_load_br_survey_gold",
        conn_id="mssql_gold",
        sql="sql/gold/load_data_survey_BR_GOLD.sql",
        autocommit=True
)


    task1 = sql_create_db_gold
    task2 = sql_create_dims_jobs_gold
    task3 = sql_create_facts_jobs_gold
    task4 = sql_create_br_jobs_gold
    task5 = sql_create_views_jobs_gold
    task6 = sql_load_dims_jobs_gold
    task7 = sql_load_facts_jobs_gold
    task8 = sql_load_br_jobs_gold
    task9 = sql_create_dims_survey_gold
    task10 = sql_create_facts_survey_gold
    task11 = sql_create_br_survey_gold
    task12 = sql_create_views_survey_gold
    task13 = sql_load_dims_survey_gold
    task14 = sql_load_facts_survey_gold
    task15 = sql_load_br_survey_gold

    task1 >> task2 >> task3 >> task4 >> task5 >> task6 >> task7 >> task8 >> task9 >> task10 >> task11 >> task12 >> task13 >> task14 >> task15
