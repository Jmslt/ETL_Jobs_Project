import polars as ps
import resources.schema_override_jobs

schema_lf = resources.schema_override_jobs.set_schema_jobs(resources.schema_override_jobs.list_columns)


#Need to ignore errors
#df = ps.scan_ndjson("./data/sample_jobs_tech.jsonl", ignore_errors=True)
df = ps.scan_ndjson("~/projects/data_tfe/jobs/freehire_jobs_part_000.jsonl", ignore_errors=False, schema_overrides=schema_lf)
df = df.select(resources.schema_override_jobs.list_columns).filter(ps.col("is_tech") == True).collect()
df.write_ndjson("./data/sample_jobs_tech.jsonl")
