Running the pipeline or the Dags 'TFE_download_<jobs or survey>_data' will create 2 sub-directories:
- jobs (contains the jobs .jsonl)
- survey (contains the survey .csv)

After initial execution of the pipeline, there should be (by default):
- 3 .jsonl files in jobs
- 4 .csv files in survey


If this data folder is not created before executing the docker compose up, the symlink between Airflow's container's
/opt/airflow/data and this data/ folder is not operational.

This symlink lets anyone inspect the data outside of the pipeline and the container without having to download the data
again on their computer.
