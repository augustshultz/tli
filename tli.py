import cmd
from get_all_projects import get_all_projects


class TLI(cmd.Cmd):
    prompt = 'tli → '
    intro = 'Welcome to tli, a command line interface to interact with Todoist. Type help or ? to list commands.\n'

    def do_projects(self, arg):
        """Get a list of your projects."""
        get_all_projects()

    def do_exit(self, args):
        """Exit the TLI tool."""
        return True


if __name__ == '__main__':
    TLI().cmdloop()
