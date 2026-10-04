# SQL SERVER ON LINUX

https://github.com/mkleehammer/pyodbc/issues/1133

https://learn.microsoft.com/fr-fr/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver17&tabs=ubuntu18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline


https://learn.microsoft.com/en-us/sql/linux/install-upgrade/quickstart-install-docker?view=sql-server-ver17&tabs=cli&pivots=cs1-bash

https://learn.microsoft.com/en-us/sql/linux/containers/configure?view=sql-server-ver17&pivots=cs1-bash#persist

--

# AIRFLOW ON LINUX

For now, using full dev image: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/

Ideally we craft our own slim image following these instructions and modifying the docker-compose to
remove what we don't need:

https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html

https://github.com/apache/airflow/discussions/29398

https://github.com/apache/airflow/discussions/34674

https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html

https://airflow.apache.org/docs/docker-stack/build.html
