import re


class Parser:
    _schema = None

    def define_schema(self, schema):
        self._schema = schema

    def parse_arguments(self, arguments: str):
        args = re.split(r' ', arguments)
        # no schema defined
        if self._schema is None:
            raise Exception("Exception: No schema is defined")

        # empty case
        if arguments == '':
            # convert the data type to a list
            return self._schema

        new_schema = self._schema
        for i in range(0, len(args)):
            arg = args[i]

            # find flag in schema that matches arg
            for flag in new_schema:

                # Outer block, if arg is a flag
                if re.fullmatch(flag[1], arg):
                    # If there are 2 or more values after a flag
                    if (i+2) < len(args):
                        if self.is_a_flag(args[i+1]) is False and self.is_a_flag(args[i+2]) is False:
                            print(arg + '\n' + args[i+1] + '\n' + args[i+2])
                            raise Exception("Exception: Two or more values were passed after a flag")

                    # If flag is a boolean
                    if isinstance(flag[2], bool):
                        flag[2] = True

                    # if flag's type is int and not the subclass of boolean
                    if isinstance(flag[2], int) and not isinstance(flag[2], bool):
                        if args[i+1].isnumeric():
                            flag[2] = int(args[i+1])

                    # If flag takes a string
                    elif isinstance(flag[2], str) and (i+1) < len(args):
                            flag[2] = args[i+1]

        return new_schema

    def find_flag_in_table(self, arg: str):
        for flag in self._schema:
            if re.fullmatch(flag[1], arg):
                return flag

    def is_a_flag(self, arg: str):
        # characters minus plus a-Z define an argument
        # args_regex = r'-[a-zA-Z]'
        for flag in self._schema:
            if re.fullmatch(flag[1], arg):
                return True
        return False