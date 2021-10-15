import re
from typing import NamedTuple


class Arg(NamedTuple):
    name: str
    type: str


class Parser:
    _schema = None

    def __init__(self):
        None

    def define_schema(self, schema):
        self._schema = schema

    def parse_argument(self, arguments: str):

        # # Not all strings in the flag format are strings
        # # Only defining the examples to start
        # schema = [
        #     ('Log', r'-[l]'),
        #     ('Port', r'-[p]'),
        #     ('Directory', r'-[d]'),
        # ]
        pass

    def parse_flags(self, arguments: str):
        # characters minus plus a-Z define an argument
        args_regex = r'-[a-zA-Z]'

        # returns all substrings matching the regex
        return re.findall(args_regex, arguments)

    def parse_values(self, arguments: str):

        args_regex = r'-[a-zA-Z]'
        spaces_regex = r' '

        values_not_flags = list()

        for element in re.split(spaces_regex, arguments):
            if (re.fullmatch(args_regex, element)) is None:
                values_not_flags.append(element)

        return values_not_flags

    def parse_flag_return_types(self, arguments):
        flags_with_return_types = list()

        for flag in self._schema:
            flags_with_return_types.append((flag[0], flag[2]))

        return flags_with_return_types

