import argparse
import requests
import config


def close_task():
    parser = argparse.ArgumentParser()
    parser.add_argument('task_id', help="The id of the task to be deleted.")

    arguments = parser.parse_args()

    response = requests.post(f"https://api.todoist.com/rest/v1/tasks/{arguments.task_id}/close",
                             headers={
                                 "Authorization": f"Bearer {config.api_token}"
                             })

    if response.status_code == 204:
        print('Successfully closed the task.')
    else:
        print('Something went wrong')


if __name__ == '__main__':
    close_task()
