import cmd

from create_task import create_task
from get_all_projects import get_all_projects
from get_tasks import get_tasks


class TLI(cmd.Cmd):
    prompt = 'tli → '
    intro = 'Welcome to tli, a command line interface to interact with Todoist. Type help or ? to list commands.\n'

    @staticmethod
    def do_projects(_):
        """Get a list of your projects."""
        projects = get_all_projects()
        [print(project) for project in projects]

    @staticmethod
    def do_inbox(_):
        """Get tasks in the inbox."""
        projects = get_all_projects()
        inbox, *_ = filter(lambda project: project.inbox, projects)
        tasks = get_tasks(project_id=inbox.project_id)
        for task in tasks:
            print(task)

    @staticmethod
    def do_task(arg):
        """Create a task in the inbox."""
        create_task(task_name=arg)

    @staticmethod
    def do_exit(_):
        """Exit the TLI tool."""
        return True


if __name__ == '__main__':
    TLI().cmdloop()
