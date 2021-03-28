import requests
import uuid
import json
import config
import argparse

from models import Task


def create_task(*, task_name: str) -> Task:
    headers = {
        'Content-Type': 'application/json',
        'X-Request-Id': str(uuid.uuid4()),
        'Authorization': f'Bearer {config.api_token}'
    }
    data = json.dumps({
        'content': task_name,
    })
    url = 'https://api.todoist.com/rest/v1/tasks'
    response = requests.post(url, data=data, headers=headers)
    if response.status_code != 200:
        raise Exception(response.reason)
    return Task(**response.json())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('task_name', help="The name of the task to be created.")
    arguments = parser.parse_args()
    task = create_task(task_name=arguments.task_name)
    print(task)
