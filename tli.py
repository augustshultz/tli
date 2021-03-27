import cmd
from get_all_projects import get_all_projects


class TLI(cmd.Cmd):
    prompt = 'tli → '
    intro = 'Welcome to tli, a command line interface to interact with Todoist. Type help or ? to list commands.\n'

    @staticmethod
    def do_projects(_):
        """Get a list of your projects."""
        projects = get_all_projects()
        [print(project) for project in projects]

    @staticmethod
    def do_exit(_):
        """Exit the TLI tool."""
        return True


if __name__ == '__main__':
    TLI().cmdloop()
