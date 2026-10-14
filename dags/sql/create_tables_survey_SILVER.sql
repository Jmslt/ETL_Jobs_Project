USE silver_tfe
GO

IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'survey')
	BEGIN
		EXEC ('CREATE SCHEMA survey')
	END
GO

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_answers')
	BEGIN
		CREATE TABLE survey.survey_answers (
			answer_id INT UNIQUE NOT NULL,
			ResponseId INT NOT NULL,
			survey_year INT,
            MainBranch VARCHAR(500),
            Age VARCHAR(255),
            EdLevel VARCHAR(500),
            Employment VARCHAR(500),
            WorkExp INT,
            LearnCode VARCHAR(2000),
            DevType VARCHAR(2000),
            OrgSize VARCHAR(255),
            ICorPM VARCHAR(255),
            RemoteWork VARCHAR(255),
            Country VARCHAR(255),
            Currency VARCHAR(255),
            CompTotal BIGINT,
            ConvertedCompYearly BIGINT,
            CONSTRAINT FK_survey_answers PRIMARY KEY (answer_id)
		)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_programming_languages')
	BEGIN
		CREATE TABLE survey.survey_programming_languages (
			answer_id INT NOT NULL,
			ResponseId INT NOT NULL,
			survey_year INT,
			[language] VARCHAR(255),
			worked_with BIT,
			want_to_work_with BIT
			CONSTRAINT FK_survey_programming_languages FOREIGN KEY (answer_id)
				REFERENCES survey.survey_answers (answer_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_databases')
	BEGIN
		CREATE TABLE survey.survey_databases (
			answer_id INT NOT NULL,
			ResponseId INT NOT NULL,
			survey_year INT,
			[database] VARCHAR(255),
			worked_with BIT,
			want_to_work_with BIT,
			CONSTRAINT FK_survey_databases FOREIGN KEY (answer_id)
				REFERENCES survey.survey_answers (answer_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_platforms')
	BEGIN
		CREATE TABLE survey.survey_platforms (
			answer_id INT NOT NULL,
			responseId INT NOT NULL,
			survey_year INT,
			platform VARCHAR(255),
			worked_with BIT,
			want_to_work_with BIT,
			CONSTRAINT FK_survey_platforms FOREIGN KEY (answer_id)
				REFERENCES survey.survey_answers (answer_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_web_frameworks')
	BEGIN
		CREATE TABLE survey.survey_web_frameworks (
			answer_id INT NOT NULL,
			responseId INT NOT NULL,
			survey_year INT,
			web_framework VARCHAR(255),
			worked_with BIT,
			want_to_work_with BIT,
			CONSTRAINT FK_survey_web_frameworks FOREIGN KEY (answer_id)
				REFERENCES survey.survey_answers (answer_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_misc_techs')
	BEGIN
		CREATE TABLE survey.survey_misc_techs (
			answer_id INT NOT NULL,
			responseId INT NOT NULL,
			survey_year INT,
			misc_tech VARCHAR(255),
			worked_with BIT,
			want_to_work_with BIT,
			CONSTRAINT FK_survey_misc_techs FOREIGN KEY (answer_id)
				REFERENCES survey.survey_answers (answer_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'survey_tools_tech')
	BEGIN
		CREATE TABLE survey.survey_tools_tech (
			answer_id INT NOT NULL,
			responseId INT NOT NULL,
			survey_year INT,
			tool_tech VARCHAR(255),
			worked_with BIT,
			want_to_work_with BIT,
			CONSTRAINT FK_survey_tools_tech FOREIGN KEY (answer_id)
				REFERENCES survey.survey_answers (answer_id)
	)
	END
