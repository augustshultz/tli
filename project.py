class Project:

    def __init__(self, **kwargs):
        if 'name' not in kwargs:
            raise TypeError('Missing "name" a required argument')
        self.name = kwargs['name']
        self.project_id = kwargs['id'] if 'id' in kwargs else None

    def __str__(self):
        output: [str] = []
        if self.project_id:
            output.append(str(self.project_id))
        output.append(self.name)
        return ' '.join(output)
