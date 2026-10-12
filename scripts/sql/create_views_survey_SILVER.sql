USE silver_tfe
GO

CREATE VIEW survey.vw_survey_answers
AS
SELECT 
		answer_id,
		ResponseId,
		survey_year,
        MainBranch,
        Age,
        EdLevel,
        Employment,
        CAST(WorkExp AS INT) as WorkExp,
        LearnCode,
        DevType,
        OrgSize,
        ICorPM,
        RemoteWork,
        Country,
        Currency,
        CAST(CompTotal AS BIGINT) AS CompTotal,
        CAST(ConvertedCompYearly AS BIGINT) AS ConvertedCompYearly
FROM bronze_tfe.dbo.survey_answers;


CREATE VIEW survey.vw_survey_databases
AS
	SELECT 	b_databases.answer_id,
			b_databases.ResponseId,
			b_databases.survey_year,
			b_databases.[database],
			b_databases.worked_with,
			b_databases.want_to_work_with
	FROM bronze_tfe.dbo.survey_databases as b_databases
	JOIN bronze_tfe.dbo.survey_answers as b_answers
		ON b_databases.answer_id = b_answers.answer_id;

CREATE VIEW survey.vw_survey_misc_techs
AS
	SELECT 	b_misc.answer_id,
			b_misc.ResponseId,
			b_misc.survey_year,
			b_misc.misc_tech,
			b_misc.worked_with,
			b_misc.want_to_work_with
	FROM bronze_tfe.dbo.survey_misc_techs as b_misc
	JOIN bronze_tfe.dbo.survey_answers as b_answers
		ON b_misc.answer_id = b_answers.answer_id;
		

CREATE VIEW survey.vw_survey_platforms
AS
	SELECT 	b_platform.answer_id,
			b_platform.ResponseId,
			b_platform.survey_year,
			b_platform.platform,
			b_platform.worked_with,
			b_platform.want_to_work_with
	FROM bronze_tfe.dbo.survey_platforms as b_platform
	JOIN bronze_tfe.dbo.survey_answers as b_answers
		ON b_platform.answer_id = b_answers.answer_id;
		
CREATE VIEW survey.vw_survey_languages
AS
	SELECT 	b_languages.answer_id,
			b_languages.ResponseId,
			b_languages.survey_year,
			b_languages.language,
			b_languages.worked_with,
			b_languages.want_to_work_with
	FROM bronze_tfe.dbo.survey_programming_languages as b_languages
	JOIN bronze_tfe.dbo.survey_answers as b_answers
		ON b_languages.answer_id = b_answers.answer_id;
		
CREATE VIEW survey.vw_survey_tools_tech
AS
	SELECT 	b_tools.answer_id,
			b_tools.ResponseId,
			b_tools.survey_year,
			b_tools.tool_tech,
			b_tools.worked_with,
			b_tools.want_to_work_with
	FROM bronze_tfe.dbo.survey_tools_tech as b_tools
	JOIN bronze_tfe.dbo.survey_answers as b_answers
		ON b_tools.answer_id = b_answers.answer_id;
		
CREATE VIEW survey.vw_survey_web_frameworks
AS
	SELECT 	b_web.answer_id,
			b_web.ResponseId,
			b_web.survey_year,
			b_web.web_framework,
			b_web.worked_with,
			b_web.want_to_work_with
	FROM bronze_tfe.dbo.survey_web_frameworks as b_web
	JOIN bronze_tfe.dbo.survey_answers as b_answers
		ON b_web.answer_id = b_answers.answer_id;
