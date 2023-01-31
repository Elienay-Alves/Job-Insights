from functools import lru_cache
from typing import Dict, List
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf8") as file:
        file_reader = csv.DictReader(file)
        return list(file_reader)


def get_unique_job_types(path: str) -> List[str]:
    data_jobs = read(path)
    type_jobs = [job["job_type"] for job in data_jobs]
    return list(set(type_jobs))
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job['job_type'] == job_type]
    raise NotImplementedError
