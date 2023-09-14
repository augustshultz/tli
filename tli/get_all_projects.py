from typing import Iterator

import config
from api import Api
from models import Project


def get_all_projects() -> list[Project]:
    status_code, results = Api(api_token=config.api_token).get(path="projects")
    if status_code != 200:
        raise Exception("Error fetching all projects.")
    return [Project(**result) for result in results]


if __name__ == "__main__":
    projects = get_all_projects()
    for project in projects:
        print(project)
