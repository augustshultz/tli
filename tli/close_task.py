import argparse

import requests

import config
from api import close_task_url


def close_task(*, task_id):
    url = close_task_url(task_id=task_id)
    headers = {"Authorization": f"Bearer {config.api_token}"}
    response = requests.post(url, headers=headers)

    if response.status_code != 204:
        raise Exception(f"Failed to close task: {task_id}")
    print(f"Closed task: {task_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("task_id", help="The id of the task to be closed.")
    arguments = parser.parse_args()
    try:
        close_task(task_id=arguments.task_id)
    except Exception as e:
        print(str(e))
