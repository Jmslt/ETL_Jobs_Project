docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Admin12345!" \
   -p 1435:1433 --name sql_tfe --hostname sql_tfe \
   -d \
   mcr.microsoft.com/mssql/server:2025-latest

#If on WSL, to connect from host: localhost,1435
