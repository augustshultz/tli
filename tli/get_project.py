import argparse

import requests

import config
from models import Project
from urls import get_project_url


def get_project(project_id: str) -> Project:
    url = get_project_url(project_id=project_id)
    headers = {"Authorization": f"Bearer {config.api_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error fetching project: {project_id}")
    return Project(**response.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_id")

    arguments = parser.parse_args()
    try:
        project = get_project(project_id=arguments.project_id)
        print(project)
    except Exception as e:
        print(e)
