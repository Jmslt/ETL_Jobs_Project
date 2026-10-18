IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'BR_programming_languages')
	BEGIN
		CREATE TABLE survey.BR_programming_languages (
			BR_prog_language_id INT IDENTITY,
			programming_language_id INT,
			answer_id INT
			CONSTRAINT PK_BR_survey_programming_languages PRIMARY KEY (BR_prog_language_id),
			CONSTRAINT FK_BR_survey_language_id FOREIGN KEY (programming_language_id)
				REFERENCES survey.DIM_programming_languages (programming_language_id),
			CONSTRAINT FK_BR_language_answer_id FOREIGN KEY (answer_id)
				REFERENCES survey.FACTS_survey_answers (answer_id)
	)
	END
	

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'BR_dbs')
	BEGIN
		CREATE TABLE survey.BR_dbs (
			BR_db_id INT IDENTITY,
			db_id INT,
			answer_id INT
			CONSTRAINT PK_BR_survey_dbs PRIMARY KEY (BR_db_id),
			CONSTRAINT FK_BR_survey_db_id FOREIGN KEY (db_id)
				REFERENCES survey.DIM_dbs (db_id),
			CONSTRAINT FK_BR_db_answer_id FOREIGN KEY (answer_id)
				REFERENCES survey.FACTS_survey_answers (answer_id)
	)
	END
	
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'BR_platforms')
	BEGIN
		CREATE TABLE survey.BR_platforms (
			BR_platform_id INT IDENTITY,
			platform_id INT,
			answer_id INT
			CONSTRAINT PK_BR_survey_platforms PRIMARY KEY (BR_platform_id),
			CONSTRAINT FK_BR_survey_platform_id FOREIGN KEY (platform_id)
				REFERENCES survey.DIM_platforms (platform_id),
			CONSTRAINT FK_BR_platform_answer_id FOREIGN KEY (answer_id)
				REFERENCES survey.FACTS_survey_answers (answer_id)
	)
	END
	
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'BR_web_frameworks')
	BEGIN
		CREATE TABLE survey.BR_web_frameworks (
			BR_web_framework_id INT IDENTITY,
			web_framework_id INT,
			answer_id INT
			CONSTRAINT PK_BR_web_frameworks PRIMARY KEY (BR_web_framework_id),
			CONSTRAINT FK_BR_web_frameworks_id FOREIGN KEY (web_framework_id)
				REFERENCES survey.DIM_web_frameworks (web_framework_id),
			CONSTRAINT FK_BR_web_frameworks_answer_id FOREIGN KEY (answer_id)
				REFERENCES survey.FACTS_survey_answers (answer_id)
	)
	END
	
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'BR_misc_techs')
	BEGIN
		CREATE TABLE survey.BR_misc_techs (
			BR_misc_tech_id INT IDENTITY,
			misc_tech_id INT,
			answer_id INT
			CONSTRAINT PK_BR_misc_techs PRIMARY KEY (BR_misc_tech_id),
			CONSTRAINT FK_BR_misc_techs_id FOREIGN KEY (misc_tech_id)
				REFERENCES survey.DIM_misc_techs (misc_tech_id),
			CONSTRAINT FK_BR_misc_techs_answer_id FOREIGN KEY (answer_id)
				REFERENCES survey.FACTS_survey_answers (answer_id)
	)
	END
	
	IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'BR_misc_tools')
	BEGIN
		CREATE TABLE survey.BR_misc_tools (
			BR_misc_tool_id INT IDENTITY,
			misc_tool_id INT,
			answer_id INT
			CONSTRAINT PK_BR_misc_tools PRIMARY KEY (BR_misc_tool_id),
			CONSTRAINT FK_BR_misc_tools_id FOREIGN KEY (misc_tool_id)
				REFERENCES survey.DIM_misc_tools (misc_tool_id),
			CONSTRAINT FK_BR_misc_tools_answer_id FOREIGN KEY (answer_id)
				REFERENCES survey.FACTS_survey_answers (answer_id)
	)
	END