SELECT DISTINCT pl1.answer_id , pl1.[language]  
FROM survey_programming_languages as pl1
JOIN survey_programming_languages as pl2
	ON pl1.answer_id = pl2.answer_id 
Where pl1.worked_with = 'True' AND pl2.want_to_work_with = 'True'


SELECT *
FROM survey_programming_languages 
WHERE answer_id = 70