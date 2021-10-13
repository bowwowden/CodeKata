import unittest

from src.parser import Parser


class MyTestCase(unittest.TestCase):

    def test_parse_arguments(self):
        arguments: str = "-l -d 8080 -d /usr/var"

        parser: Parser = Parser()

        flags = parser.parse_flags(arguments)

        print(flags)

        expected_args = ['-l', '-d', '-d']

        self.assertEqual(flags, expected_args)



if __name__ == '__main__':
    unittest.main()
