USE gold_tfe

INSERT INTO survey.DIM_programming_languages 
	SELECT *
	FROM survey.vw_DIM_survey_languages;

INSERT INTO survey.DIM_dbs
	SELECT *
	FROM survey.vw_DIM_dbs;

INSERT INTO survey.DIM_platforms
	SELECT *
	FROM survey.vw_DIM_platforms;

INSERT INTO survey.DIM_web_frameworks
	SELECT *
	FROM survey.vw_DIM_web_frameworks;

INSERT INTO survey.DIM_misc_techs
	SELECT *
	FROM survey.vw_DIM_misc_techs;

INSERT INTO survey.DIM_misc_tools
	SELECT *
	FROM survey.vw_DIM_misc_tools;