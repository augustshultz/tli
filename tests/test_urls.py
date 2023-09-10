from urls import delete_task_url, get_project_url, close_task_url


def test_delete_task_url():
    task_id = "4677084901"
    expected = f"https://api.todoist.com/rest/v2/tasks/{task_id}"
    assert delete_task_url(task_id=task_id) == expected


def test_get_project_url():
    project_id = 2203306141
    expected = f"https://api.todoist.com/rest/v2/projects/{project_id}"
    assert get_project_url(project_id=project_id) == expected


def test_close_task_url():
    task_id = "4677084901"
    expected = f"https://api.todoist.com/rest/v2/tasks/{task_id}/close"
    assert close_task_url(task_id=task_id) == expected
