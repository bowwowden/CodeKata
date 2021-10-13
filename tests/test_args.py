import unittest

from src.parser import Parser


class MyTestCase(unittest.TestCase):

    def test_parse_arguments(self):
        arguments: str = "-l -p 8080 -d /usr/var"

        parser: Parser = Parser()

        flags = parser.parse_flags(arguments)

        print(flags)

        expected_args = ['-l', '-p', '-d']

        self.assertEqual(flags, expected_args)

    def test_parse_values(self):
        arguments: str = "-l -p 8080 -d /usr/var"

        parser: Parser = Parser()

        values = parser.parse_values(arguments)

        print(values)

        expected_values = ['8080', '/usr/var']

        self.assertEqual(values, expected_values)

    def test_parse_return_values_for_undefined_args(self):
        arguments: str = "-p 8080 -d /usr/var"

        # in this test, it should return false for logging
        # this return is because the -l flag is not used

        parser: Parser = Parser()

        parsed_args_values = parser.parse_argument()

        expected_values = ["LOGGING:FALSE", "PORT:8080", "DIRECTORY:/usr/var"]

        self.assertEqual(expected_values, parsed_args_values)


if __name__ == '__main__':
    unittest.main()
