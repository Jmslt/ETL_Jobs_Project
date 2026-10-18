IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'gold_tfe')
	BEGIN
		CREATE DATABASE gold_tfe
  END
