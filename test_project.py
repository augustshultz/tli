import pytest

from models import Project


def test_create_project_with_name():
    p = Project(name='This is a name!')
    assert p.name == 'This is a name!'


def test_creation_of_project_without_name_throws_value_error():
    with pytest.raises(TypeError) as e:
        Project()
    assert str(e.value) == 'Missing "name" a required argument'


def test_project_with_id():
    project_id = 17
    p = Project(name='This is a name!', id=project_id)
    assert p.project_id == project_id


def test_project_str():
    p = Project(name='This is a name!', id=17)
    assert str(p) == '17 This is a name!'


def test_project_str_without_id():
    p = Project(name='This is a name!')
    assert str(p) == 'This is a name!'
