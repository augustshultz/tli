class Project:

    def __init__(self, **kwargs):
        if 'name' not in kwargs:
            raise TypeError('Missing "name" a required argument')
        self.name = kwargs['name']
        if 'id' in kwargs:
            self.project_id = kwargs['id']
