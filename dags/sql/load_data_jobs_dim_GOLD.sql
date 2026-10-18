USE gold_tfe

INSERT INTO jobs.DIM_jobs_details
	SELECT *
	FROM jobs.vw_DIM_jobs_details;

INSERT INTO jobs.DIM_jobs_skills
	SELECT jobs_skill_name
	FROM jobs.vw_DIM_jobs_skills;


INSERT INTO jobs.DIM_jobs_categories
	SELECT jobs_category_name
	FROM jobs.vw_DIM_categories;
	
INSERT INTO jobs.DIM_jobs_countries 
	SELECT country_name
	FROM jobs.vw_DIM_jobs_countries;