class Task:

    def __init__(self, content, completed=False, **kwargs):
        self.content = content
        self.completed = completed

    def __str__(self):
        return self.content