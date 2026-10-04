#!/bin/bash

mkdir ~/.sqlvolumes

docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=Admin12345!' \
-p 1433:1433 \
--name sql1 --hostname sql_server_1 \
-d \
-v ~/.sqlvolumes/data:/var/opt/mssql/data \
-v ~/.sqlvolumes/log:/var/opt/mssql/log \
-v ~/.sqlvolumes/secrets:/var/opt/mssql/secrets \
-d mcr.microsoft.com/mssql/server:2025-latest
