import cmd
from get_all_projects import get_all_projects


class TLI(cmd.Cmd):
    prompt = 'tli '

    def do_projects(self, arg):
        """Get a list of your projects."""
        get_all_projects()


if __name__ == '__main__':
    TLI().cmdloop()
