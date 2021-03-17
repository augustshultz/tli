import pytest

from project import Project


def test_create_project_with_name():
    p = Project(name='This is a name!')
    assert p.name == 'This is a name!'

def test_creation_of_project_without_name_throws_value_error():
    with pytest.raises(TypeError) as e:
        Project()
    assert str(e.value) == 'Missing "name" a required argument'
