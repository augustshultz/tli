from typing import Iterator

import requests
import config
from models import Project


def get_all_projects() -> Iterator[Project]:
    url = 'https://api.todoist.com/rest/v2/projects'
    headers = {'Authorization': f'Bearer {config.api_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception('Error fetching all projects.')
    return map(lambda kwargs: Project(**kwargs), response.json())


if __name__ == '__main__':
    projects = get_all_projects()
    for project in projects:
        print(project)
