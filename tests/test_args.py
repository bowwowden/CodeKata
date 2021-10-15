import unittest

from src.parser import Parser


class MyTestCase(unittest.TestCase):
    parser: Parser

    def setUp(self) -> None:
        self.parser: Parser = Parser()

        # Defining the schema in the setup
        schema = [
            ('Log', r'-[l]', 'boolean'),
            ('Port', r'-[p]', 'integer'),
            ('Directory', r'-[d]', 'string'),
        ]

        self.parser.define_schema(schema)

    def test_parse_arguments(self):
        arguments: str = "-l -p 8080 -d /usr/var"

        flags = self.parser.parse_flags(arguments)

        print(flags)

        expected_args = ['-l', '-p', '-d']

        self.assertEqual(flags, expected_args)

    def test_parse_argument_return_types(self):
        arguments: str = "-l -p 8080 -d /usr/var"

        flags_with_return_types = self.parser.parse_flag_return_types(arguments)

        print(flags_with_return_types)

        expected_args = [('Log', 'boolean'), ('Port', 'integer'), ('Directory', 'string')]

        self.assertEqual(flags_with_return_types, expected_args)

    def test_parse_values(self):
        arguments: str = "-l -p 8080 -d /usr/var"

        values = self.parser.parse_values(arguments)

        print(values)

        expected_values = ['8080', '/usr/var']

        self.assertEqual(values, expected_values)

    def test_parse_return_values_for_undefined_args(self):
        arguments: str = "-p 8080 -d /usr/var"

        # in this test, it should return false for logging
        # this return is because the -l flag is not used

        parsed_args_values = self.parser.parse_argument(arguments)
        for token in parsed_args_values:
            print(token)

        expected_values = ["LOGGING:FALSE", "PORT:8080", "DIRECTORY:/usr/var"]

        self.assertEqual(expected_values, parsed_args_values)


if __name__ == '__main__':
    unittest.main()
