import argparse
import requests
import config

parser = argparse.ArgumentParser()
parser.add_argument('task_id', help="The id of the task to be deleted.")

arguments = parser.parse_args()

response = requests.delete(f"https://api.todoist.com/rest/v1/tasks/{arguments.task_id}",
                           headers={
                               "Authorization": f"Bearer {config.api_token}"
                           })

if response.status_code == 204:
    print('Successfully deleted task.')
else:
    print('Something went wrong')
