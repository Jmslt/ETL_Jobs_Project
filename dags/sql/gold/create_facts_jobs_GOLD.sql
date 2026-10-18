USE gold_tfe

IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'jobs')
	BEGIN
		EXEC ('CREATE SCHEMA jobs')
	END


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'FACTS_jobs_postings')
	BEGIN
		CREATE TABLE jobs.FACTS_jobs_postings (
			job_id INT,
			month_posted INT,
			job_category_id INT,
			experience_years_min INT,
			CONSTRAINT PK_jobs_postings PRIMARY KEY (job_id),
			CONSTRAINT FK_FACTS_jobs_category FOREIGN KEY (job_category_id)
				REFERENCES jobs.DIM_jobs_categories (jobs_category_id),
			CONSTRAINT FK_FACTS_jobs_details FOREIGN KEY (job_id)
				REFERENCES jobs.DIM_jobs_details(job_id),
	)
	END