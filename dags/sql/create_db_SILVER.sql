IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'silver_tfe')
	BEGIN
		CREATE DATABASE silver_tfe
  END
