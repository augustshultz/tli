from typing import NewType, Any

import requests

from models import Project

StatusCode = NewType("StatusCode", int)


class Api:
    host = "https://api.todoist.com/rest/v2/"

    def __init__(self, *, api_token: str):
        self.api_token = api_token

    def get(self, *, path: str) -> tuple[StatusCode, Any]:
        headers = {"Authorization": f"Bearer {self.api_token}"}
        response = requests.get(self.host + path, headers=headers)
        return StatusCode(response.status_code), response.json()

    def projects(self) -> list[Project]:
        status_code, results = self.get(path="projects")
        if status_code != 200:
            raise Exception("Error fetching all projects.")
        return [Project(**result) for result in results]


def delete_task_url(*, task_id: int) -> str:
    return f"{_endpoint}tasks/{task_id}"


def close_task_url(*, task_id: int) -> str:
    return f"{_endpoint}tasks/{task_id}/close"


def get_project_url(*, project_id: int) -> str:
    return f"{_endpoint}projects/{project_id}"


_endpoint: str = "https://api.todoist.com/rest/v2/"
