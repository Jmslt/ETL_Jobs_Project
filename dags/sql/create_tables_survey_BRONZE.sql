USE bronze_tfe


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_answers')
	BEGIN
		CREATE TABLE survey_answers (
			answer_id INT UNIQUE NOT NULL,
			ResponseId INT NOT NULL,
			survey_year VARCHAR(4),
            MainBranch VARCHAR(500),
            Age VARCHAR(255),
            EdLevel VARCHAR(500),
            Employment VARCHAR(500),
            WorkExp VARCHAR(500),
            LearnCode VARCHAR(2000),
            DevType VARCHAR(2000),
            OrgSize VARCHAR(255),
            ICorPM VARCHAR(255),
            RemoteWork VARCHAR(255),
            Country VARCHAR(255),
            Currency VARCHAR(255),
            CompTotal VARCHAR(255),
            ConvertedCompYearly VARCHAR(255)
		)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_programming_languages')
	BEGIN
		CREATE TABLE survey_programming_languages (
			answer_id INT NOT NULL,
			ResponseId INT NOT NULL,
			survey_year VARCHAR(4),
			[language] VARCHAR(255),
			worked_with VARCHAR(10),
			want_to_work_with VARCHAR(10)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_databases')
	BEGIN
		CREATE TABLE survey_databases (
			answer_id INT NOT NULL,
			ResponseId INT NOT NULL,
			survey_year VARCHAR(4),
			[database] VARCHAR(255),
			worked_with VARCHAR(10),
			want_to_work_with VARCHAR(10)			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_platforms')
	BEGIN
		CREATE TABLE survey_platforms (
			answer_id INT NOT NULL,
			responseId INT NOT NULL,
			survey_year VARCHAR(4),
			platform VARCHAR(255),
			worked_with VARCHAR(10),
			want_to_work_with VARCHAR(10)			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_web_frameworks')
	BEGIN
		CREATE TABLE survey_web_frameworks (
			answer_id INT NOT NULL,
			responseId INT NOT NULL,
			survey_year VARCHAR(4),
			web_framework VARCHAR(255),
			worked_with VARCHAR(10),
			want_to_work_with VARCHAR(10)			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_misc_techs')
	BEGIN
		CREATE TABLE survey_misc_techs (
			answer_id INT NOT NULL,
			responseId INT NOT NULL,
			survey_year VARCHAR(4),
			misc_tech VARCHAR(255),
			worked_with VARCHAR(10),
			want_to_work_with VARCHAR(10)			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_tools_tech')
	BEGIN
		CREATE TABLE survey_tools_tech (
			answer_id INT NOT NULL,
			responseId INT NOT NULL,
			survey_year VARCHAR(4),
			tool_tech VARCHAR(255),
			worked_with VARCHAR(10),
			want_to_work_with VARCHAR(10)			
	)
	END
