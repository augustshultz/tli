import argparse
import requests
import config
from models import Task


def get_task(task_id: str) -> Task:
    url = f"https://api.todoist.com/rest/v1/tasks/{task_id}"
    headers = {'Authorization': f'Bearer {config.api_token}'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f'Failed to get task: {task_id}')

    return Task(**response.json())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='The id of the task to get.')

    arguments = parser.parse_args()

    try:
        task = get_task(task_id=arguments.id)
        print(task)
    except Exception as e:
        print(e)
