#!/usr/bin/python
import unittest

from climb.completer import Completer, current_argument


class CompleterTest(unittest.TestCase):

    def test_current_argument(self):
        tests = [
            (("any_command ", 12, 12), (1, "")),
            (("any_command /any/path /foo/bar/baz", 0, 3), (0, "any")),
            (("any_command /any/path /foo/bar/baz", 0, 11), (0, "any_command")),

            (("any_command /any/path /foo/bar/baz", 13, 13), (1, "/")),
            (("any_command /any/path /foo/bar/baz", 13, 14), (1, "/a")),
            (("any_command /any/path /foo/bar/baz", 13, 16), (1, "/any")),
            (("any_command /any/path /foo/bar/baz", 17, 17), (1, "/any/")),

            (("any_command /any/path /foo/bar/baz", 17, 21), (1, "/any/path")),
            (("any_command /any/path/ /foo/bar/baz", 22, 22), (1, "/any/path/")),

            (("any_command /any/path /foo/bar/baz", 31, 34), (2, "/foo/bar/baz")),
            (("any_command /any/path /foo/bar/baz/", 35, 35), (2, "/foo/bar/baz/")),

            (("any_command /any/path /foo/bar/baz", 27, 30), (2, "/foo/bar")),
            (("any_command /any/path /foo/bar/baz", 31, 31), (2, "/foo/bar/")),

            (("any_command /any/path /foo/bar/baz", 23, 26), (2, "/foo")),
            (("any_command /any/path /foo/bar/baz", 27, 27), (2, "/foo/")),
        ]

        for args, expected in tests:
            result = current_argument(*args)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
