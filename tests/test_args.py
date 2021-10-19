import unittest
from dataclasses import dataclass

from src.parser import Parser


class MyTestCase(unittest.TestCase):
    parser: Parser

    def setUp(self) -> None:
        self.parser: Parser = Parser()

        # Defining the schema in the setup
        schema: list = [
            ['Log', r'-[l]', False],
            ['Port', r'-[p]', 0],
            ['Directory', r'-[d]', ''],
        ]

        self.parser.define_schema(schema)

    def test_schema_is_undefined(self):
        self.parser.define_schema(None)

        self.assertIsNone(self.parser._schema)

        arguments: str = ""

        with self.assertRaises(Exception):
            self.parser.parse_arguments(arguments)

    def test_parse_empty_arguments(self):
        arguments: str = ""

        parsed_args_values = self.parser.parse_arguments(arguments)

        expected_values: list = [
            ['Log', r'-[l]', False],
            ['Port', r'-[p]', 0],
            ['Directory', r'-[d]', ''],
        ]

        self.assertEqual(expected_values, parsed_args_values)

    def test_parse_single_boolean_flag(self):
        arguments: str = "-l"

        parsed_args_values = self.parser.parse_arguments(arguments)

        expected_values: list = [
            ['Log', r'-[l]', True],
            ['Port', r'-[p]', 0],
            ['Directory', r'-[d]', ''],
        ]

        self.assertEqual(expected_values, parsed_args_values)

    def test_parse_multiple_boolean_flags(self):
        arguments: str = "-l -l -l"

        parsed_args_values = self.parser.parse_arguments(arguments)

        expected_values: list = [
            ['Log', r'-[l]', True],
            ['Port', r'-[p]', 0],
            ['Directory', r'-[d]', ''],
        ]

        self.assertEqual(expected_values, parsed_args_values)

    def test_parse_return_values_for_undefined_args(self):
        arguments: str = "-p 8080 -d /usr/var"

        # in this test, it should return false for logging
        # this return is because the -l flag is not used

        parsed_args_values = self.parser.parse_arguments(arguments)

        expected_values: list = [
            ['Log', r'-[l]', False],
            ['Port', r'-[p]', 8080],
            ['Directory', r'-[d]', '/usr/var'],
        ]

        self.assertEqual(expected_values, parsed_args_values)

    def test_parse_return_values_many_duplicates(self):
        arguments: str = "-l -l -l -z -p 8080 -d /usr/var"

        parsed_args_values = self.parser.parse_arguments(arguments)

        expected_values: list = [
            ['Log', r'-[l]', True],
            ['Port', r'-[p]', 8080],
            ['Directory', r'-[d]', '/usr/var'],
        ]

        self.assertEqual(expected_values, parsed_args_values)

    def test_parse_too_many_values_after_flag(self):
        # Tests if there is more than one value after the flag
        arguments: str = "-l -l -l -p 8080 8080 -d /usr/var"

        # Throws Exception in case there are too many
        with self.assertRaises(Exception):
            self.parser.parse_arguments(arguments)



if __name__ == '__main__':
    unittest.main()
