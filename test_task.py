import json
from models import Task


def test_task_creation_succeeds_with_just_content():
    task = Task('Test content')
    assert task.content == 'Test content'


def test_task_creation_with_full_json_response():
    with open('sample-task.json') as file:
        task_response = json.load(file)
    task = Task(**task_response)
    assert task.content == task_response['content']
    assert not task.completed


def test_readable_task_str():
    task = Task('Test content', id=1)
    assert str(task) == '1 Test content'
