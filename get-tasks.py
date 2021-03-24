import argparse
import requests
import config
from models import Task

parser = argparse.ArgumentParser()
parser.add_argument('--project', '-p')

arguments = parser.parse_args()

response = requests.get(
    'https://api.todoist.com/rest/v1/tasks',
    params={
        'project_id': f'{arguments.project}'
    },
    headers={
        'Authorization': f'Bearer {config.api_token}'
    }).json()

tasks = [Task(**kwargs) for kwargs in response]
for task in tasks:
    print(task)
