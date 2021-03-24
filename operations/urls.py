def delete_task_url(*, task_id):
    return f'https://api.todoist.com/rest/v1/tasks/{task_id}'


def get_project_url(*, project_id):
    return f'https://api.todoist.com/rest/v1/projects/{project_id}'
