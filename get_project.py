import argparse
import json

import requests
import config
from urls import get_project_url

parser = argparse.ArgumentParser()
parser.add_argument('project_id')

arguments = parser.parse_args()

response = requests.get(
    get_project_url(project_id=arguments.project_id),
    headers={
        'Authorization': f'Bearer {config.api_token}'
    }).json()

print(json.dumps(response, indent=1))
