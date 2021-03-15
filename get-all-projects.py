import requests
import config

projects = requests.get(
    "https://api.todoist.com/rest/v1/projects",
    headers={
        "Authorization": f'Bearer {config.api_token}'
    }
).json()

print(projects)
