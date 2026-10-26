import os

import polars as pl


REPO_URL = "https://github.com/StackExchange/Survey/raw/refs/heads/main/packages/archive/"
SURVEY_YEARS = ["2022", "2023", "2024", "2025"]

def download_survey_csv():
    for index, year in enumerate(SURVEY_YEARS):
        csv_url = REPO_URL + year + "/results.csv"
        dir_path = "/opt/airflow/data/survey"
        csv_path = "/opt/airflow/data/survey/" + year + ".csv"
        os.makedirs(dir_path, exist_ok=True)
        survey_df = pl.read_csv(source=csv_url)
        survey_df.write_csv(file=csv_path, separator=",")

if __name__ == "__main__":
    download_survey_csv()
