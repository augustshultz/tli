import argparse
import requests
from typing import List

import config
from models import Task


def get_tasks_from_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id', '-p')
    parser.add_argument('--filter', '-f')
    arguments = parser.parse_args()
    get_tasks(
        project_id=arguments.project_id,
        tasks_filter=arguments.filter
    )


def get_tasks(*, project_id=None, tasks_filter: str = None) -> List[Task]:
    params = {}
    if project_id:
        params['project_id'] = project_id
    if tasks_filter:
        params['filter'] = tasks_filter

    response = requests.get(
        'https://api.todoist.com/rest/v1/tasks',
        params=params,
        headers={
            'Authorization': f'Bearer {config.api_token}'
        }).json()
    return [Task(**kwargs) for kwargs in response]


if __name__ == '__main__':
    get_tasks_from_arguments()
