USE gold_tfe

INSERT INTO survey.FACTS_survey_answers
	SELECT *
	FROM jobs.vw_FACTS_survey_answers;