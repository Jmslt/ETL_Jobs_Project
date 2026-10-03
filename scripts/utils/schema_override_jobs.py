import polars as ps

list_columns = ['public_slug',
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

schema_dict = {}

def set_schema_jobs(list_columns):
    for col in list_columns:
        schema_dict.update({col: ps.String})
    return schema_dict

