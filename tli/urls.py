_endpoint: str = "https://api.todoist.com/rest/v2/"


def delete_task_url(*, task_id: int) -> str:
    return f"{_endpoint}tasks/{task_id}"


def close_task_url(*, task_id: int) -> str:
    return f"{_endpoint}tasks/{task_id}/close"


def get_project_url(*, project_id: int) -> str:
    return f"{_endpoint}projects/{project_id}"
