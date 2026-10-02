# coding: utf-8
import pandas as pd

list_col_names = [
'source',
'title',
'company_slug',
'posted_at',
'updated_at',
'closed_at',
'countries',
'work_mode',
'skills',
'is_tech',
'seniority',
'category',
'posting_language',
'employment_type',
'experience_years_min',
'company_name',
'company_industries',
'company_types',
'company_sizes',
'domains']

df = pd.read_json("./data/sample_jobs.jsonl", lines=True)
df_tech = df.loc[df["is_tech"] == True, list_col_names ]
df_tech.to_json("./data/sample_jobs_tech.jsonl", orient="records", lines=True)
