USE bronze_tfe
GO


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'jobs_data')
	BEGIN
		CREATE TABLE jobs_data (
			public_slug NVARCHAR(MAX),
			[source] NVARCHAR(MAX),
			title NVARCHAR(MAX),
			company NVARCHAR(MAX),
			company_slug NVARCHAR(MAX),
			location NVARCHAR(MAX),
			description NVARCHAR(MAX),
			url NVARCHAR(MAX),
			posted_at NVARCHAR(MAX),
			created_at NVARCHAR(MAX),
			updated_at NVARCHAR(MAX),
			closed_at NVARCHAR(MAX),
			countries NVARCHAR(MAX),
			regions NVARCHAR(MAX),
			work_mode NVARCHAR(MAX),
			skills NVARCHAR(MAX),
			cities NVARCHAR(MAX),
			collections NVARCHAR(MAX),
			is_tech NVARCHAR(MAX),
			seniority NVARCHAR(MAX),
			category NVARCHAR(MAX),
			posting_language NVARCHAR(MAX),
			employment_type NVARCHAR(MAX),
			education_level NVARCHAR(MAX),
			english_level NVARCHAR(MAX),
			experience_years_min NVARCHAR(MAX),
			salary_min NVARCHAR(MAX),
			salary_max NVARCHAR(MAX),
			salary_currency NVARCHAR(MAX),
			salary_period NVARCHAR(MAX),
			company_name NVARCHAR(MAX),
			company_tagline NVARCHAR(MAX),
			company_industries NVARCHAR(MAX),
			company_hq_country NVARCHAR(MAX),
			company_types NVARCHAR(MAX),
			company_sizes NVARCHAR(MAX),
			domains NVARCHAR(MAX),
			yc_batch NVARCHAR(MAX),
			yc_status NVARCHAR(MAX),
			yc_stage NVARCHAR(MAX),
			yc_flags NVARCHAR(MAX)			
	)
	END