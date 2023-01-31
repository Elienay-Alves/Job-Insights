from functools import lru_cache
from typing import Dict, List
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, econding="utf8") as file:
        file_reader = csv.DictReader(file)
        return list(file_reader)


def get_unique_job_types(path: str) -> List[str]:
   data_jobs = read(path)
   type_jobs = [job["job_type"] for job in data_jobs]
   return list(set(type_jobs))
   raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
