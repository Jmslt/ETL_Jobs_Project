CREATE VIEW jobs.vw_jobs_postings
AS
SELECT 
		job_id,
		public_slug,
		source,
		title,
		company,
		company_slug,
		location,
		description,
		CAST((SUBSTRING(posted_at, 0, 20)) AS DATETIME) AS posted_at,
		CAST((SUBSTRING(created_at, 0, 20)) AS DATETIME) AS created_at,
		CAST((SUBSTRING(updated_at, 0, 20)) AS DATETIME) AS updated_at,
		CAST((SUBSTRING(closed_at, 0, 20)) AS DATETIME) AS closed_at,
		regions,
		work_mode,
		seniority,
		category,
		employment_type,
		posting_language,
		education_level,
		english_level,
		CAST(experience_years_min AS INT) as experience_years_min,
		CAST(salary_min AS INT) as salary_min,
		CAST(salary_max AS INT) as salary_max,
		salary_currency,
		salary_period,
		company_hq_country
FROM bronze_tfe.dbo.jobs_postings
WHERE is_tech = 'true';


CREATE VIEW jobs.vw_jobs_cities
AS
	SELECT b_cities.job_id, b_cities.cities
	FROM bronze_tfe.dbo.jobs_cities as b_cities
	JOIN bronze_tfe.dbo.jobs_postings as b_postings
		ON b_cities.job_id = b_postings.job_id
	WHERE b_postings.is_tech = 'true';

CREATE VIEW jobs.vw_jobs_company_industries
AS
	SELECT b_industries.job_id, b_industries.company_industries
	FROM bronze_tfe.dbo.jobs_company_industries as b_industries
	JOIN bronze_tfe.dbo.jobs_postings as b_postings
		ON b_industries.job_id = b_postings.job_id
	WHERE b_postings.is_tech = 'true';

CREATE VIEW jobs.vw_jobs_company_sizes
AS
	SELECT b_sizes.job_id, b_sizes.company_sizes
	FROM bronze_tfe.dbo.jobs_company_sizes as b_sizes
	JOIN bronze_tfe.dbo.jobs_postings as b_postings
		ON b_sizes.job_id = b_postings.job_id
	WHERE b_postings.is_tech = 'true';


CREATE VIEW jobs.vw_jobs_company_types
AS
	SELECT b_types.job_id, b_types.company_types
	FROM bronze_tfe.dbo.jobs_company_types as b_types
	JOIN bronze_tfe.dbo.jobs_postings as b_postings
		ON b_types.job_id = b_postings.job_id
	WHERE b_postings.is_tech = 'true';


CREATE VIEW jobs.vw_jobs_countries
AS
	SELECT b_countries.job_id, b_countries.countries
	FROM bronze_tfe.dbo.jobs_countries as b_countries
	JOIN bronze_tfe.dbo.jobs_postings as b_postings
		ON b_countries.job_id = b_postings.job_id
	WHERE b_postings.is_tech = 'true';



CREATE VIEW jobs.vw_jobs_skills
AS
	SELECT b_skills.job_id, b_skills.skills
	FROM bronze_tfe.dbo.jobs_skills as b_skills
	JOIN bronze_tfe.dbo.jobs_postings as b_postings
		ON b_skills.job_id = b_postings.job_id
	WHERE b_postings.is_tech = 'true';
