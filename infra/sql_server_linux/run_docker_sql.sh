docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Admin12345!" \
   -p 1435:1433 --name sql1 --hostname sql1 \
   -d \
   mcr.microsoft.com/mssql/server:2025-latest

#If on WSL, to connect from host SSMS: localhost,1435
