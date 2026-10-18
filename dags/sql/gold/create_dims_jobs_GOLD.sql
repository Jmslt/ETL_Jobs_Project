USE gold_tfe

IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'jobs')
	BEGIN
		EXEC ('CREATE SCHEMA jobs')
	END


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DIM_jobs_skills')
	BEGIN
		CREATE TABLE jobs.DIM_jobs_skills (
			jobs_skill_id INT IDENTITY,
			jobs_skill_name VARCHAR(255),
			CONSTRAINT PK_jobs_skills PRIMARY KEY (jobs_skill_id)
	)
	END

	
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DIM_jobs_categories')
	BEGIN
		CREATE TABLE jobs.DIM_jobs_categories (
			jobs_category_id INT IDENTITY,
			jobs_category_name VARCHAR(500),
			CONSTRAINT PK_jobs_categories PRIMARY KEY (jobs_category_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DIM_countries')
	BEGIN
		CREATE TABLE jobs.DIM_jobs_countries (
			country_id INT IDENTITY,
			country_name VARCHAR(255),
			CONSTRAINT PK_countries PRIMARY KEY (country_id)
	)
	END
	

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'DIM_jobs_details')
	BEGIN
		CREATE TABLE jobs.DIM_jobs_details (
			job_id INT,
			job_title VARCHAR(1000),
			posted_at DATETIME,
			closed_at DATETIME,
			seniority VARCHAR(10),
			employment_type VARCHAR(20),
			salary_min INT,
			salary_max INT,
			salary_currency VARCHAR(100),
			salary_period VARCHAR(10)
			CONSTRAINT PK_jobs_details PRIMARY KEY (job_id)
	)
	END