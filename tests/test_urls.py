from operations.urls import delete_task_url


def test_delete_task_url():
    task_id = '4677084901'
    expected = f'https://api.todoist.com/rest/v1/tasks/{task_id}'
    assert delete_task_url(task_id=task_id) == expected
