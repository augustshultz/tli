from datetime import date

from typing import Optional


class Project:
    def __init__(self, **kwargs):
        if "name" not in kwargs:
            raise TypeError('Missing "name" a required argument')
        self.name: str = kwargs["name"]
        self.inbox: bool = kwargs.get("is_inbox_project", False)
        self.project_id = kwargs["id"] if "id" in kwargs else None

    def __str__(self):
        output: list[str] = []
        if self.project_id:
            output.append(str(self.project_id))
        output.append(self.name)
        return " ".join(output)


class Due:
    def __init__(self, **kwargs):
        self.recurring = kwargs.get("recurring", False)
        self.string = kwargs.get("string", None)
        if "date" in kwargs:
            self.date = date.fromisoformat(kwargs["date"])

    def __str__(self):
        return self.string


class Task:
    def __init__(self, content: str, completed: bool = False, priority: int = 1, **kwargs):
        if priority < 1 or priority > 4:
            raise TypeError("Invalid priority must be 1, 2, 3, or 4")
        self.content = content
        self.priority = priority
        self.task_id = kwargs["id"] if "id" in kwargs else None
        self.completed = completed
        self.due: Optional[Due] = (
            Due(**kwargs["due"]) if "due" in kwargs and kwargs["due"] else None
        )

    def __str__(self):
        values: list[str] = [str(self.task_id), self.content]
        if self.due:
            values.append(str(self.due))
        return " ".join(values)
