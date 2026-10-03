# coding: utf-8
import polars as ps
lf = ps.scan_ndjson("/home/jm/projects/tfe/jobs_data/cp_freehire_jobs_part_000.jsonl")
lf.collect()
