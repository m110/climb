#!/usr/bin/python
import unittest

from climb.commands import Commands, command, completers


class DummyCommands(Commands):

    @command
    @completers('any_completer', 'second_completer')
    def test(self, any_arg, second_arg):
        return 'any_result'


class CommandsTest(unittest.TestCase):

    def test_command_decorator(self):
        self.assertEqual(DummyCommands.test.command, True)

    def test_completers_decorator(self):
        self.assertEqual(DummyCommands.test.completers, ('any_completer', 'second_completer'))

    def test_execute(self):
        commands = DummyCommands(None)
        result = commands.execute('test', any_arg=None, second_arg=None)
        self.assertEqual(result, 'any_result')


if __name__ == "__main__":
    unittest.main()
