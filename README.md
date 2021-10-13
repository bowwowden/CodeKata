# CodeKata
Each branch contains an exercise, which is solved by TDD that generates a matching production code module with it.

## Kata 001

This is the first Kata exercise, taken from https://codingdojo.org/kata/Args/. You must create a program that parses arguments from the command line, much like you would find in running terminal commands, ex. -l -p 8080 -d /usr/logs. 
The arguments consist of:
* Flags: one character, preceded by a minus sign -
* Values: arguments to be passed to flags, coming in amounts of 0 or 1 values. 

This program should generate a parser for the arguments. These arguments are delimited by spaces or tabs for instance that separate them as distinct values.

This program also should generate a schema which describes the expected arguments. It specifies the number and types of flags and values the program expects.

After the schema has been specified, the program passes the argument to the parser. This parser verifies that the arguments passed will correctly map to the schema.

This example of arguments, -l -p 8080 -d /usr/logs 
indicates a schema of 3 flags: l,p,d. 
* L takes no values, it is a boolean flag. 
* P is a port flag and takes an integer value
* D is a directory flag that takes a string value

Not all flags in the schema necessarily have to be passed as arguments. If such a flag is not passed, still return its value, for instance, 
a boolean will return False, an integer will return 0, and a string will return "".

