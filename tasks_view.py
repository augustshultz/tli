from typing import List, Tuple

from rich.console import Console
from rich.table import Table

from models import Task


def print_tasks(tasks: List[Task]):
    table = Table()

    table.add_column("ID")
    table.add_column("Content")
    table.add_column("Due")
    table.add_column("Priority")

    for task in tasks:
        table.add_row(*task_row(task))

    console = Console()
    console.print(table)


def task_row(task: Task) -> Tuple[str, str, str, str]:
    return f'{task.task_id}', task.content, str(task.due) if task.due else '', f'{task.priority}'
