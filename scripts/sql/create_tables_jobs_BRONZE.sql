USE bronze_tfe
GO


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_postings')
	BEGIN
		CREATE TABLE jobs_postings (
			job_id INT UNIQUE NOT NULL,
			public_slug NVARCHAR(4000),
			[source] NVARCHAR(255),
			title NVARCHAR(1000),
			company NVARCHAR(255),
			company_slug NVARCHAR(255),
			[location] NVARCHAR(4000),
			[description] NVARCHAR(MAX),
			[url] NVARCHAR(2000),
			posted_at NVARCHAR(100),
			created_at NVARCHAR(100),
			updated_at NVARCHAR(100),
			closed_at NVARCHAR(100),
			regions VARCHAR(255),
			work_mode NVARCHAR(255),
			collections VARCHAR(255),
			is_tech VARCHAR(10),
			seniority NVARCHAR(255),
			category NVARCHAR(1000),
			posting_language NVARCHAR(10),
			employment_type NVARCHAR(255),
			education_level NVARCHAR(50),
			english_level NVARCHAR(10),
			experience_years_min NVARCHAR(10),
			salary_min NVARCHAR(100),
			salary_max NVARCHAR(100),
			salary_currency NVARCHAR(100),
			salary_period NVARCHAR(50),
			company_name NVARCHAR(255),
			company_tagline NVARCHAR(1000),
			company_hq_country NVARCHAR(255),
			yc_batch VARCHAR(255),
			yc_status VARCHAR(255),
			yc_stage VARCHAR(255),
			yc_flags VARCHAR(255)			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_countries')
	BEGIN
		CREATE TABLE jobs_countries (
			job_id INT,
			countries VARCHAR(1000),			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_skills')
	BEGIN
		CREATE TABLE jobs_skills (
			job_id INT,
			skills VARCHAR(1000),			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_cities')
	BEGIN
		CREATE TABLE jobs_cities (
			job_id INT,
			cities VARCHAR(1000),			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_company_industries')
	BEGIN
		CREATE TABLE jobs_company_industries (
			job_id INT,
			company_industries VARCHAR(1000),			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_company_types')
	BEGIN
		CREATE TABLE jobs_company_types (
			job_id INT,
			company_types VARCHAR(1000),			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_company_sizes')
	BEGIN
		CREATE TABLE jobs_company_sizes (
			job_id INT,
			company_sizes VARCHAR(1000),			
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_company_domains')
	BEGIN
		CREATE TABLE jobs_company_domains (
			job_id INT,
			[domains] VARCHAR(1000),			
	)
	END
