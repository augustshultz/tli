class Task:

    def __init__(self, content, completed=False, **kwargs):
        self.content = content
        self.task_id = kwargs['id'] if 'id' in kwargs else None
        self.completed = completed

    def __str__(self):
        return f'{self.task_id} {self.content}'
