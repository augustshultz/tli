from project import Project


def test_create_project_with_name():
    p = Project(name='This is a name!')
    assert p.name == 'This is a name!'