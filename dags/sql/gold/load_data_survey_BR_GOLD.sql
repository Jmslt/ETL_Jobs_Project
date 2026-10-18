USE gold_tfe

INSERT INTO survey.BR_programming_languages 
	SELECT *
	FROM survey.vw_BR_survey_languages;

INSERT INTO survey.BR_dbs
	SELECT *
	FROM survey.vw_BR_dbs;

INSERT INTO survey.BR_platforms 
	SELECT *
	FROM survey.vw_BR_platforms;

INSERT INTO survey.BR_web_frameworks
	SELECT *
	FROM survey.vw_BR_web_frameworks;

INSERT INTO survey.BR_misc_techs
	SELECT *
	FROM survey.vw_BR_misc_techs;

INSERT INTO survey.BR_misc_tools
	SELECT *
	FROM survey.vw_BR_misc_tools;