USE gold_tfe

INSERT INTO jobs.FACTS_jobs_postings
	SELECT *
	FROM jobs.vw_FACTS_jobs_postings;