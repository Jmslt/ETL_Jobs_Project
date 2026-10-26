import gzip
import shutil
import os

from huggingface_hub import hf_hub_download

REPO_ID = "istrelov/freehire-jobs"

def download_archives_huggingface():
    file_numbers = [3,7]
    for number, file in enumerate(file_numbers):
        hf_hub_download(repo_id=REPO_ID, filename=f"freehire_jobs_part_00{file}.jsonl.gz", repo_type="dataset",
                    local_dir="/opt/airflow/data/jobs/archives")

def unzip_archives_jobs():
    for file in os.scandir("/opt/airflow/data/jobs/archives"):
        if file.name.endswith("gz"):
            with gzip.open(file, "rb") as archive:
                with open(f'/opt/airflow/data/jobs/{file.name.replace(".gz", "")}', "wb") as jsonl_file:
                    shutil.copyfileobj(archive, jsonl_file)
                    print(f"Jsonl file created: {jsonl_file}")


def delete_archives_huggingface():
    shutil.rmtree("/opt/airflow/data/jobs/archives")
