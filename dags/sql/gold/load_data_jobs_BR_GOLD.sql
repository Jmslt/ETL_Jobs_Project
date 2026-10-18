USE tfe_gold

INSERT INTO jobs.BR_jobs_skills
	SELECT skill_id, job_id
	FROM jobs.vw_BR_jobs_skills;

INSERT INTO jobs.BR_jobs_countries 
	SELECT country_id, job_id
	FROM jobs.vw_BR_jobs_countries;