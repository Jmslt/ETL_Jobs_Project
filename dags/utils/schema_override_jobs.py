from sqlalchemy import NVARCHAR, String
import polars as pl


list_columns_complete = ['public_slug',
                'source',
                'title',
                'company',
                'company_slug',
                'location',
                'description',
                'url',
                'posted_at',
                'created_at',
                'updated_at',
                'closed_at',
                'countries',
                'regions',
                'work_mode',
                'skills',
                'cities',
                'collections',
                'is_tech',
                'seniority',
                'category',
                'posting_language',
                'employment_type',
                'education_level',
                'english_level',
                'experience_years_min',
                'salary_min',
                'salary_max',
                'salary_currency',
                'salary_period',
                'company_name',
                'company_tagline',
                'company_industries',
                'company_hq_country',
                'company_types',
                'company_sizes',
                'domains',
                'yc_batch',
                'yc_status',
                'yc_stage',
                'yc_flags']

#TODO refactor to generate this with a function
schema_columns_pd = {'public_slug': NVARCHAR,
                'source': NVARCHAR,
                'title': NVARCHAR,
                'company': NVARCHAR,
                'company_slug': NVARCHAR,
                'location': NVARCHAR,
                'description': NVARCHAR,
                'url': NVARCHAR,
                'posted_at': NVARCHAR,
                'created_at': NVARCHAR,
                'updated_at': NVARCHAR,
                'closed_at': NVARCHAR,
                'countries': String,
                'regions': NVARCHAR,
                'work_mode': String,
                'skills': NVARCHAR,
                'cities': NVARCHAR,
                'collections': NVARCHAR,
                'is_tech': String,
                'seniority': NVARCHAR,
                'category': NVARCHAR,
                'posting_language': NVARCHAR,
                'employment_type': NVARCHAR,
                'education_level': NVARCHAR,
                'english_level': NVARCHAR,
                'experience_years_min': NVARCHAR,
                'salary_min': NVARCHAR,
                'salary_max': NVARCHAR,
                'salary_currency': NVARCHAR,
                'salary_period': NVARCHAR,
                'company_name': NVARCHAR,
                'company_tagline': NVARCHAR,
                'company_industries': String,
                'company_hq_country': NVARCHAR,
                'company_types': String,
                'company_sizes': String,
                'domains': String,
                'yc_batch': String,
                'yc_status': String,
                'yc_stage': String,
                'yc_flags': String}

schema_complete_pl = {}

def get_schema_jobs_pl():
    for col in list_columns_complete:
        schema_complete_pl.update({col: pl.String})
    return schema_complete_pl

def get_schema_nolist(schema_complete):
    list_col_remove = ["countries", "skills", "cities", "company_industries", "company_types", "company_sizes", "domains"]
    schema_no_list = schema_complete.copy()
    for col in list_col_remove:
        schema_no_list.pop(col)

    return schema_no_list

