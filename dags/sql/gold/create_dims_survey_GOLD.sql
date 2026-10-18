USE gold_tfe

IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'survey')
	BEGIN
		EXEC ('CREATE SCHEMA survey')
	END


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DIM_programming_languages')
	BEGIN
		CREATE TABLE survey.DIM_programming_languages (
			programming_language_id INT IDENTITY,
			programming_language_name VARCHAR(255),
			CONSTRAINT PK_DIM_languages PRIMARY KEY (programming_language_id)
	)
	END

	
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DIM_dbs')
	BEGIN
		CREATE TABLE survey.DIM_dbs (
			db_id INT IDENTITY,
			db_name VARCHAR(500),
			CONSTRAINT PK_DIM_dbs PRIMARY KEY (db_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DIM_platforms')
	BEGIN
		CREATE TABLE survey.DIM_platforms (
			platform_id INT IDENTITY,
			platform_name VARCHAR(255),
			CONSTRAINT PK_DIM_platforms PRIMARY KEY (platform_id)
	)
	END
	
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DIM_web_frameworks')
	BEGIN
		CREATE TABLE survey.DIM_web_frameworks (
			web_framework_id INT IDENTITY,
			web_framework_name VARCHAR(255),
			CONSTRAINT PK_DIM_web_frameworks PRIMARY KEY (web_framework_id)
	)
	END
	
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DIM_misc_techs')
	BEGIN
		CREATE TABLE survey.DIM_misc_techs (
			misc_tech_id INT IDENTITY,
			misc_tech_name VARCHAR(255),
			CONSTRAINT PK_DIM_misc_techs PRIMARY KEY (misc_tech_id)
	)
	END
	
	
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DIM_misc_tools')
	BEGIN
		CREATE TABLE survey.DIM_misc_tools (
			misc_tool_id INT IDENTITY,
			misc_tool_name VARCHAR(255),
			CONSTRAINT PK_DIM_misc_tools PRIMARY KEY (misc_tool_id)
	)
	END
