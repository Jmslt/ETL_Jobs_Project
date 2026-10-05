import polars as pl

from utils.schema_override_jobs import list_columns, set_schema_jobs

SchemaStr = set_schema_jobs(list_columns)
lf = pl.scan_ndjson("/home/jm/projects/data_tfe/jobs_raw/freehire_jobs_part_013.jsonl", schema=SchemaStr)

lf.collect_schema()
