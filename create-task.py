import requests
import uuid
import json
import config

requests.post(
    "https://api.todoist.com/rest/v1/tasks",
    data=json.dumps({
        "content": "Tester",
    }),
    headers={
        "Content-Type": "application/json",
        "X-Request-Id": str(uuid.uuid4()),
        'Authorization': f'Bearer {config.api_token}'
    }).json()
