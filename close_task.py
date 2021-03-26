import argparse
import requests
import config


def close_task_with_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('task_id', help='The id of the task to be deleted.')

    arguments = parser.parse_args()
    close_task(task_id=arguments.task_id)


def close_task(*, task_id):
    url = f'https://api.todoist.com/rest/v1/tasks/{task_id}/close'
    response = requests.post(
        url,
        headers={
            'Authorization': f'Bearer {config.api_token}'
        }
    )

    if response.status_code == 204:
        print('Successfully closed the task.')
    else:
        print('Something went wrong')


if __name__ == '__main__':
    close_task_with_arguments()
