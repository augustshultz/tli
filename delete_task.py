import argparse
import requests
import config
from urls import delete_task_url


def delete_task(*, task_id):
    url = delete_task_url(task_id=task_id)
    headers = {'Authorization': f'Bearer {config.api_token}'}
    response_status = requests.delete(url, headers=headers).status_code

    if response_status != 204:
        raise Exception(f'Failed to delete task: {task_id}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('task_ids', nargs='+', help='The id(s) of the task(s) to be deleted.')
    arguments = parser.parse_args()
    task_ids = arguments.task_ids
    for a_task_id in task_ids:
        try:
            delete_task(task_id=a_task_id)
        except Exception as e:
            print(str(e))
