## Initial exploratory analysis for TFE validation

- Sample in 'sample_jobs.jsonl' consisting of a thousand lines of data for job postings (https://freehire.me/)
- Samples in 'sample_stackoverflow_2025_survey.csv' consisting of raw survey data from Stack Overflow Survey 2025 (https://github.com/StackExchange/Survey/tree/main/packages/archive/2025)


## Business questions

- What is the proportion of IT jobs and their specific fields?
- What are the jobs that pay the best? Which companies give a salary rangem and which ones do not?
- What is the difference between the IT landscape Skills in demand VS the skills professionals have/want in the survey?

## First try at Modelization

3 FACTS tables:
    - Jobs analysis = all jobs in the data
    - Salary analysis = for all jobs
    - IT Skills landscape = to compare Jobs Skills vs Professionals Survey Skills

This is to give a rough ideas of how many tables we wll be able to create and how they might be related to each other.

I will add the fields if I have the time before 11/09/2026.

## Tools I plan to use

Extract + Transform:
    - Polars = Data is too big, I need to use Lazyframes

Load:
    - Apache Airflow = orchestrator
        - Will call pure SQL scripts to create the DB Model and Load the data