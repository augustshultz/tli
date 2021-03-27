import argparse
import json

import requests
import config
from urls import get_project_url


def get_project(project_id):
    url = get_project_url(project_id=project_id)
    headers = {'Authorization': f'Bearer {config.api_token}'}
    response = requests.get(url, headers=headers).json()
    print(json.dumps(response, indent=1))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('project_id')

    arguments = parser.parse_args()
    get_project(project_id=arguments.project_id)
