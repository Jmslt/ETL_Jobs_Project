USE gold_tfe

IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'survey')
	BEGIN
		EXEC ('CREATE SCHEMA survey')
	END


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'FACTS_survey_answers')
	BEGIN
		CREATE TABLE survey.FACTS_survey_answers (
			answer_id INT,
			answer_year INT,
			main_category VARCHAR(500),
			dev_type VARCHAR(2000)
			CONSTRAINT PK_survey_skills PRIMARY KEY (answer_id)
	)
	END