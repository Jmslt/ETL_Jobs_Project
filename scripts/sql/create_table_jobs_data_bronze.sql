USE bronze_tfe
GO


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_data')
	BEGIN
		CREATE TABLE jobs_data (
			public_slug VARCHAR(255),
			[source] VARCHAR(255),
			title VARCHAR(255),
			company VARCHAR(255),
			company_slug VARCHAR(255),
			location VARCHAR(255),
			description VARCHAR(MAX),
			url VARCHAR(MAX),
			posted_at VARCHAR(50),
			created_at VARCHAR(50),
			updated_at VARCHAR(50),
			closed_at VARCHAR(50),
			countries VARCHAR(255),
			regions VARCHAR(255),
			work_mode VARCHAR(255),
			skills VARCHAR(MAX),
			cities VARCHAR(255),
			collections VARCHAR(255),
			is_tech VARCHAR(10),
			seniority VARCHAR(255),
			category VARCHAR(MAX),
			posting_language VARCHAR(50),
			employment_type VARCHAR(255),
			education_level VARCHAR(50),
			english_level VARCHAR(50),
			experience_years_min VARCHAR(50),
			salary_min VARCHAR(50),
			salary_max VARCHAR(50),
			salary_currency VARCHAR(10),
			salary_period VARCHAR(50),
			company_name VARCHAR(255),
			company_tagline VARCHAR(MAX),
			company_industries VARCHAR(MAX),
			company_hq_country VARCHAR(255),
			company_types VARCHAR(255),
			company_sizes VARCHAR(255),
			domains VARCHAR(MAX),
			yc_batch VARCHAR(50),
			yc_status VARCHAR(50),
			yc_stage VARCHAR(50),
			yc_flags VARCHAR(50)			
	)
	END