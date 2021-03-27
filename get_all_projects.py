import requests
import config
from models import Project


def get_all_projects():
    url = 'https://api.todoist.com/rest/v1/projects'
    headers = {'Authorization': f'Bearer {config.api_token}'}
    response = requests.get(url, headers=headers).json()
    projects = map(lambda kwargs: Project(**kwargs), response)
    [print(project) for project in projects]


if __name__ == '__main__':
    get_all_projects()
