USE bronze_tfe
GO


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_data')
	BEGIN
		CREATE TABLE jobs_data (
			public_slug NVARCHAR(4000),
			[source] NVARCHAR(255),
			title NVARCHAR(1000),
			company NVARCHAR(255),
			company_slug NVARCHAR(255),
			[location] NVARCHAR(1000),
			[description] NVARCHAR(MAX),
			[url] NVARCHAR(1000),
			posted_at NVARCHAR(100),
			created_at NVARCHAR(100),
			updated_at NVARCHAR(100),
			closed_at NVARCHAR(100),
			countries VARCHAR(1000),
			regions VARCHAR(255),
			work_mode NVARCHAR(255),
			skills VARCHAR(1000),
			cities VARCHAR(1000),
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
			company_industries VARCHAR(1000),
			company_hq_country NVARCHAR(255),
			company_types VARCHAR(255),
			company_sizes VARCHAR(255),
			[domains] VARCHAR(1000),
			yc_batch VARCHAR(255),
			yc_status VARCHAR(255),
			yc_stage VARCHAR(255),
			yc_flags VARCHAR(255)			
	)
	END