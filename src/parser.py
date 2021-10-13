import re


class Parser:

    def __init__(self):
        pass

    def parse_flags(self, arguments: str):

        # characters minus plus a-Z define an argument
        args_regex = '-[a-zA-Z]*'

        # returns all substrings matching the regex
        return re.findall(args_regex, arguments)

