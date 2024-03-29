import argparse
import requests
from api import delete_task_url
from config import api_token


def delete_task(*, task_id: int):
    url = delete_task_url(task_id=task_id)
    headers = {"Authorization": f"Bearer {api_token()}"}
    response_status = requests.delete(url, headers=headers).status_code

    if response_status != 204:
        raise Exception(f"Failed to delete task: {task_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "task_ids", type=int, nargs="+", help="The id(s) of the task(s) to be deleted."
    )
    arguments = parser.parse_args()
    task_ids: list[int] = arguments.task_ids
    for a_task_id in task_ids:
        try:
            delete_task(task_id=a_task_id)
        except Exception as e:
            print(str(e))
