from typing import Iterator

import config
from api import Api
from models import Project


def get_all_projects() -> list[Project]:
    return Api(api_token=config.api_token).projects()


if __name__ == "__main__":
    projects = get_all_projects()
    for project in projects:
        print(project)
