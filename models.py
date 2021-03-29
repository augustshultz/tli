from datetime import date


class Project:

    def __init__(self, **kwargs):
        if 'name' not in kwargs:
            raise TypeError('Missing "name" a required argument')
        self.name: str = kwargs['name']
        self.inbox: bool = kwargs.get('inbox_project', False)
        self.project_id = kwargs['id'] if 'id' in kwargs else None

    def __str__(self):
        output: [str] = []
        if self.project_id:
            output.append(str(self.project_id))
        output.append(self.name)
        return ' '.join(output)


class Task:

    def __init__(self, content, completed=False, **kwargs):
        self.content = content
        self.task_id = kwargs['id'] if 'id' in kwargs else None
        self.completed = completed

    def __str__(self):
        return f'{self.task_id} {self.content}'


class Due:

    def __init__(self, **kwargs):
        self.recurring = kwargs.get('recurring', False)
        self.string = kwargs.get('string', None)
        if 'date' in kwargs:
            self.date = date.fromisoformat(kwargs['date'])
