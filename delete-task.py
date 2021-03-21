import argparse
import requests
import config
from urls import delete_task_url


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('task_ids', nargs='+', help='The id(s) of the task(s) to be deleted.')
    arguments = parser.parse_args()
    task_ids = arguments.task_ids
    for task_id in task_ids:
        delete_task(task_id=task_id)


def delete_task(*, task_id):
    url = delete_task_url(task_id=task_id)
    headers = {'Authorization': f'Bearer {config.api_token}'}
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print('Successfully deleted task.')
    else:
        print('Something went wrong')


if __name__ == '__main__':
    parse_arguments()
