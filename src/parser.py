import re


class Parser:

    def __init__(self):
        pass

    def parse_argument(self, arguments: str):
        values = "blah"
        return values

    def parse_flags(self, arguments: str):
        # characters minus plus a-Z define an argument
        args_regex = r'-[a-zA-Z]*'

        # returns all substrings matching the regex
        return re.findall(args_regex, arguments)

    def parse_values(self, arguments: str):

        args_regex = r'-[a-zA-Z]*'
        spaces_regex = r' '

        values_not_flags = list()

        for element in re.split(spaces_regex, arguments):
            if (re.fullmatch(args_regex, element)) is None:
                values_not_flags.append(element)

        return values_not_flags
