CREATE VIEW jobs.vw_DIM_jobs_details
AS
	SELECT 
		job_id,
		title as [job_title],
		posted_at,
		closed_at,
		seniority,
		employment_type,
		salary_min,
		salary_max,
		salary_currency,
		salary_period
	FROM silver_tfe.jobs.jobs_postings;


CREATE VIEW jobs.vw_DIM_jobs_skills
AS
	SELECT DISTINCT skills as jobs_skill_name
	FROM silver_tfe.jobs.jobs_skills;

	
CREATE VIEW jobs.vw_BR_jobs_skills
AS
	SELECT d_skills.jobs_skill_id as skill_id,
			s_skills.job_id
	FROM jobs.DIM_jobs_skills as d_skills
		JOIN silver_tfe.jobs.jobs_skills as s_skills
			ON d_skills.jobs_skill_name = s_skills.skills;
		

CREATE VIEW jobs.vw_DIM_categories
AS
	SELECT DISTINCT category as jobs_category_name
	FROM silver_tfe.jobs.jobs_postings;
	
CREATE VIEW jobs.vw_DIM_jobs_countries
AS
	SELECT DISTINCT countries as country_name
	FROM silver_tfe.jobs.jobs_countries;


CREATE VIEW jobs.vw_BR_jobs_countries
AS
	SELECT d_countries.country_id,
			s_countries.job_id
	FROM jobs.DIM_jobs_countries as d_countries
		JOIN silver_tfe.jobs.jobs_countries as s_countries
			ON d_countries.country_name = s_countries.countries;


CREATE VIEW jobs.vw_FACTS_jobs_postings
AS
	SELECT 	
		d_details.job_id,
		MONTH(s_postings.created_at) as month_posted,
		d_categories.jobs_category_id,
		s_postings.experience_years_min
	FROM jobs.DIM_jobs_details as d_details
		JOIN silver_tfe.jobs.jobs_postings as s_postings
			ON d_details.job_id = s_postings.job_id
		JOIN jobs.DIM_jobs_categories as d_categories
			ON d_categories.jobs_category_name = s_postings.category
		
			
