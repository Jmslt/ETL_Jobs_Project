CREATE VIEW survey.vw_DIM_survey_languages
AS
	SELECT DISTINCT language as programming_language_name
	FROM silver_tfe.survey.survey_programming_languages;

	
CREATE VIEW survey.vw_BR_survey_languages
AS
	SELECT d_languages.programming_language_id as programming_language_id,
			s_languages.answer_id
	FROM survey.DIM_programming_languages as d_languages
		JOIN silver_tfe.survey.survey_programming_languages as s_languages
			ON d_languages.programming_language_name = s_languages.language;

CREATE VIEW survey.vw_DIM_dbs
AS
	SELECT DISTINCT [database] as db_name
	FROM silver_tfe.survey.survey_databases;

CREATE VIEW survey.vw_BR_dbs
AS
	SELECT d_dbs.db_id as db_id,
			s_dbs.answer_id
	FROM survey.DIM_dbs as d_dbs
		JOIN silver_tfe.survey.survey_databases as s_dbs
			ON d_dbs.db_name = s_dbs.[database];

CREATE VIEW survey.vw_DIM_platforms
AS
	SELECT DISTINCT platform as platform_name
	FROM silver_tfe.survey.survey_platforms;

CREATE VIEW survey.vw_BR_platforms
AS
	SELECT d_platforms.platform_id as platform_id,
			s_platforms.answer_id
	FROM survey.DIM_platforms as d_platforms
		JOIN silver_tfe.survey.survey_platforms as s_platforms
			ON d_platforms.platform_name = s_platforms.platform;

CREATE VIEW survey.vw_DIM_web_frameworks
AS
	SELECT DISTINCT web_framework as web_framework_name
	FROM silver_tfe.survey.survey_web_frameworks;

CREATE VIEW survey.vw_BR_web_frameworks
AS
	SELECT d_web.web_framework_id as web_framework_id,
			s_web.answer_id
	FROM survey.DIM_web_frameworks as d_web
		JOIN silver_tfe.survey.survey_web_frameworks as s_web
			ON d_web.web_framework_name = s_web.web_framework;

CREATE VIEW survey.vw_DIM_misc_techs
AS
	SELECT DISTINCT misc_tech as misc_tech_name
	FROM silver_tfe.survey.survey_misc_techs;

CREATE VIEW survey.vw_BR_misc_techs
AS
	SELECT d_techs.misc_tech_id as misc_tech_id,
			s_techs.answer_id
	FROM survey.DIM_misc_techs as d_techs
		JOIN silver_tfe.survey.survey_misc_techs as s_techs
			ON d_techs.misc_tech_name = s_techs.misc_tech;

CREATE VIEW survey.vw_DIM_misc_tools
AS
	SELECT DISTINCT tool_tech as misc_tool_name
	FROM silver_tfe.survey.survey_tools_tech;

CREATE VIEW survey.vw_BR_misc_tools
AS
	SELECT d_tools.misc_tool_id as misc_tool_id,
			s_tools.answer_id
	FROM survey.DIM_misc_tools as d_tools
		JOIN silver_tfe.survey.survey_tools_tech as s_tools
			ON d_tools.misc_tool_name = s_tools.tool_tech;


CREATE VIEW jobs.vw_FACTS_survey_answers
AS
	SELECT 	
		answer_id,
		survey_year as answer_year,
		MainBranch as main_category,
		DevType as dev_type
	FROM silver_tfe.survey.survey_answers
		
			
