from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    return max(
        [
            int(job['max_salary'])
            for job in data
            if job['max_salary'.isdigit()]
        ]
    )


def get_min_salary(path: str) -> int:
    data = read(path)
    return min(
        [
            int(job['min_salary'])
            for job in data
            if job['min_salary'].isdigit()
        ]
    )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    existence_validation = "min_salary" in job and "max_salary" in job

    if not existence_validation:
        raise ValueError

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if not (
        (type(min_salary) is str or type(min_salary) is int)
        and (type(max_salary) is str or type(max_salary) is int)
    ):
        raise ValueError
        
    min_salary = int(job["min_salary"])
    max_salary = int(job["max_salary"])

    min_max_validation = min_salary > max_salary
    if min_max_validation or not (
        type(salary) is str or type(salary) is int
    ):
        raise ValueError
    return int(min_salary) <= int(salary) <= int(max_salary)

def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    list = []
    try:
        list = [
            job
            for job in jobs
            if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
        ]
    except TypeError:
        raise ValueError("Error")
    finally:
        return list