from typing import NewType, Any

import requests

StatusCode = NewType("StatusCode", int)


class Api:
    host = "https://api.todoist.com/rest/v2/"

    def __init__(self, *, api_token: str):
        self.api_token = api_token

    def get(self, *, path: str) -> tuple[StatusCode, Any]:
        headers = {"Authorization": f"Bearer {self.api_token}"}
        response = requests.get(self.host + path, headers=headers)
        return StatusCode(response.status_code), response.json()
