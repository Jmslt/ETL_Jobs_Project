USE silver_tfe
GO

INSERT INTO jobs.jobs_postings 
	SELECT *
	FROM jobs.vw_jobs_postings;
	
INSERT INTO jobs.jobs_cities 
	SELECT *
	FROM jobs.vw_jobs_cities;

INSERT INTO jobs.jobs_company_industries
	SELECT *
	FROM jobs.vw_jobs_company_industries;

INSERT INTO jobs.jobs_company_sizes
	SELECT *
	FROM jobs.vw_jobs_company_sizes;

INSERT INTO jobs.jobs_company_types
	SELECT *
	FROM jobs.vw_jobs_company_types;

INSERT INTO jobs.jobs_countries
	SELECT *
	FROM jobs.vw_jobs_countries;

INSERT INTO jobs.jobs_skills
	SELECT *
	FROM jobs.vw_jobs_skills;