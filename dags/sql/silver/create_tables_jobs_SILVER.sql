USE silver_tfe

IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'jobs')
	BEGIN
		EXEC ('CREATE SCHEMA jobs')
	END


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_postings')
	BEGIN
		CREATE TABLE jobs.jobs_postings (
			job_id INT UNIQUE NOT NULL,
			public_slug VARCHAR(4000),
			[source] VARCHAR(255),
			title VARCHAR(1000),
			company VARCHAR(255),
			company_slug VARCHAR(255),
			[location] VARCHAR(4000),
			[description] VARCHAR(MAX),
			posted_at DATETIME,
			created_at DATETIME,
			updated_at DATETIME,
			closed_at DATETIME,
			regions VARCHAR(255),
			work_mode VARCHAR(10),
			seniority VARCHAR(10),
			category VARCHAR(500),
			posting_language VARCHAR(10),
			employment_type VARCHAR(20),
			education_level VARCHAR(10),
			english_level VARCHAR(10),
			experience_years_min INT,
			salary_min INT,
			salary_max INT,
			salary_currency NVARCHAR(100),
			salary_period VARCHAR(10),
			company_hq_country VARCHAR(255),
			CONSTRAINT PK_jobs_postings PRIMARY KEY (job_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_countries')
	BEGIN
		CREATE TABLE jobs.jobs_countries (
			id_job_countries INT IDENTITY,
			job_id INT,
			countries VARCHAR(10),
			CONSTRAINT PK_jobs_countries PRIMARY KEY (id_job_countries),
			CONSTRAINT FK_jobs_countries FOREIGN KEY (job_id)
				REFERENCES jobs.jobs_postings (job_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_skills')
	BEGIN
		CREATE TABLE jobs.jobs_skills (
			id_job_skills INT IDENTITY,
			job_id INT,
			skills VARCHAR(255),	
			CONSTRAINT PK_jobs_skills PRIMARY KEY (id_job_skills),
			CONSTRAINT FK_jobs_skills FOREIGN KEY (job_id)
				REFERENCES jobs.jobs_postings (job_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_cities')
	BEGIN
		CREATE TABLE jobs.jobs_cities (
			id_job_cities INT IDENTITY,
			job_id INT,
			cities VARCHAR(255),
			CONSTRAINT PK_jobs_cities PRIMARY KEY (id_job_cities),
			CONSTRAINT FK_jobs_cities FOREIGN KEY (job_id)
				REFERENCES jobs.jobs_postings (job_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_company_industries')
	BEGIN
		CREATE TABLE jobs.jobs_company_industries (
			id_company_industries INT IDENTITY,
			job_id INT,
			company_industries VARCHAR(500),
			CONSTRAINT PK_company_industries PRIMARY KEY (id_company_industries),
			CONSTRAINT FK_company_industries FOREIGN KEY (job_id)
				REFERENCES jobs.jobs_postings (job_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_company_types')
	BEGIN
		CREATE TABLE jobs.jobs_company_types (
			id_company_types INT IDENTITY,
			job_id INT,
			company_types VARCHAR(255),		
			CONSTRAINT PK_company_types PRIMARY KEY (id_company_types),
			CONSTRAINT FK_company_types FOREIGN KEY (job_id)
				REFERENCES jobs.jobs_postings (job_id)
	)
	END

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_company_sizes')
	BEGIN
		CREATE TABLE jobs.jobs_company_sizes (
			id_company_sizes INT IDENTITY,
			job_id INT,
			company_sizes VARCHAR(20),
			CONSTRAINT PK_company_sizes PRIMARY KEY (id_company_sizes),
			CONSTRAINT FK_company_sizes FOREIGN KEY (job_id)
				REFERENCES jobs.jobs_postings (job_id)
	)
	END
