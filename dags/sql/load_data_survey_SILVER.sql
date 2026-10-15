INSERT INTO survey.survey_answers 
	SELECT *
	FROM survey.vw_survey_answers;

INSERT INTO survey.survey_databases 
	SELECT *
	FROM survey.vw_survey_databases;

INSERT INTO survey.survey_misc_techs 
	SELECT *
	FROM survey.vw_survey_misc_techs;

INSERT INTO survey.survey_platforms 
	SELECT *
	FROM survey.vw_survey_platforms;

INSERT INTO survey.survey_programming_languages 
	SELECT *
	FROM survey.vw_survey_languages;

INSERT INTO survey.survey_tools_tech
	SELECT *
	FROM survey.vw_survey_tools_tech;

INSERT INTO survey.survey_web_frameworks
	SELECT *
	FROM survey.vw_survey_web_frameworks;
