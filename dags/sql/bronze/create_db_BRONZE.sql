IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'bronze_tfe')
	BEGIN
		CREATE DATABASE bronze_tfe
	END
