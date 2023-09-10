import requests
import uuid
import config
import argparse

from models import Task


def create_task(*, task_name: str, due: str = None) -> Task:
    headers = {
        "Content-Type": "application/json",
        "X-Request-Id": str(uuid.uuid4()),
        "Authorization": f"Bearer {config.api_token}",
    }
    data = {
        "content": task_name,
    }
    if due:
        data["due_string"] = due
    url = "https://api.todoist.com/rest/v2/tasks"
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        raise Exception(response.reason)
    return Task(**response.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("task_name", help="The name of the task.")
    parser.add_argument("--due", "-d", help="The due value for the task.")
    arguments = parser.parse_args()
    task = create_task(task_name=arguments.task_name, due=arguments.due)
    print(task)
