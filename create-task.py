import requests
import uuid
import json
import config
import argparse


def create_task_from_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('task_name', help="The name of the task to be created.")
    arguments = parser.parse_args()
    create_task(task_name=arguments.task_name)


def create_task(*, task_name):
    response = requests.post(
        'https://api.todoist.com/rest/v1/tasks',
        data=json.dumps({
            'content': task_name,
        }),
        headers={
            'Content-Type': 'application/json',
            'X-Request-Id': str(uuid.uuid4()),
            'Authorization': f'Bearer {config.api_token}'
        }).json()
    print(json.dumps(response, indent=1))


if __name__ == '__main__':
    create_task_from_arguments()
