from climb.exceptions import UnknownCommand


def command(function):
    function.command = True
    return function


class Commands(object):

    def __init__(self, cli):
        self._cli = cli
        self._commands = {}

    def execute(self, name, *args, **kwargs):
        if hasattr(self, name):
            method = getattr(self, name)
            if getattr(method, 'command', None):
                return method(*args, **kwargs)

        raise UnknownCommand("There is no action for command {}".format(command))

    @command
    def help(self, parser, all_commands, subject):
        if subject:
            subparsers = [cmd for cmd in all_commands
                          if cmd.name == subject]
            if subparsers:
                parser = subparsers[0].parser

        return parser.print_help()

    @command
    def exit(self):
        self._cli.set_running(False)
