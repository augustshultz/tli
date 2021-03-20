import requests
import config
from project import Project


def get_all_projects():
    projects = [Project(**kwargs) for kwargs in requests.get(
        "https://api.todoist.com/rest/v1/projects",
        headers={
            "Authorization": f'Bearer {config.api_token}'
        }
    ).json()]

    for project in projects:
        print(project)


if __name__ == '__main__':
    get_all_projects()
