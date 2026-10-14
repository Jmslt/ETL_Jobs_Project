#!/bin/bash

echo -e "AIRFLOW_UID=$(id -u)" > .env

# Adds your current's user UID to .env
# If no UID is set, the Airflow related folders
# (dags, plugins, logs, data) will be created as 
# root and will be read-only.
