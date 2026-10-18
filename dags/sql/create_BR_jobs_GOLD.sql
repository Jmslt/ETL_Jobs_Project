IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'BR_jobs_skills')
	BEGIN
		CREATE TABLE jobs.BR_jobs_skills (
			BR_skill_id INT IDENTITY,
			skill_id INT,
			job_id INT
			CONSTRAINT PK_BR_skills PRIMARY KEY (BR_skill_id),
			CONSTRAINT FK_BR_skill_id FOREIGN KEY (skill_id)
				REFERENCES jobs.DIM_jobs_skills (jobs_skill_id),
			CONSTRAINT FK_BR_skills_job_id FOREIGN KEY (job_id)
				REFERENCES jobs.FACTS_jobs_postings (job_id)
	)
	END
	

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'BR_jobs_countries')
	BEGIN
		CREATE TABLE jobs.BR_jobs_countries (
			BR_country_id INT IDENTITY,
			country_id INT,
			job_id INT
			CONSTRAINT PK_BR_countries PRIMARY KEY (BR_country_id),
			CONSTRAINT FK_BR_country_id FOREIGN KEY (country_id)
				REFERENCES jobs.DIM_jobs_countries (country_id),
			CONSTRAINT FK_BR_countries_job_id FOREIGN KEY (job_id)
				REFERENCES jobs.FACTS_jobs_postings (job_id)
	)
	END