import cmd

from api import Api

from create_task import create_task
from get_tasks import get_tasks
from tasks_view import print_tasks
from config import api_token


class TLI(cmd.Cmd):
    prompt = "tli → "
    intro = (
        "Welcome to tli, a command line interface to interact with Todoist. Type help or ? to"
        " list commands.\n"
    )

    @staticmethod
    def do_projects(_):
        """Get a list of your projects."""
        projects = Api(api_token=api_token()).projects()
        [print(project) for project in projects]

    @staticmethod
    def do_inbox(_):
        """Get tasks in the inbox."""
        projects = Api(api_token=api_token()).projects()
        inbox, *_ = filter(lambda project: project.inbox, projects)
        tasks = get_tasks(project_id=inbox.project_id)
        print_tasks(tasks=tasks)

    @staticmethod
    def do_task(arg):
        """Create a task in the inbox."""
        create_task(task_name=arg)

    @staticmethod
    def do_today(_):
        """Get tasks due today"""
        tasks = get_tasks(tasks_filter="today | overdue")
        print_tasks(tasks=tasks)

    @staticmethod
    def do_exit(_):
        """Exit the TLI tool."""
        return True


if __name__ == "__main__":
    TLI().cmdloop()
