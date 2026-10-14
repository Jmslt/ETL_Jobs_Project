SELECT TOP (1000) [public_slug]
      ,[source]
      ,[title]
      ,[description]
      ,[skills]

  FROM [bronze_tfe].[dbo].[jobs_data]
  WHERE skills LIKE '\[%"java"%\]' ESCAPE '\'
