# ===----------------- utils.py - Functions for output and colors -------------===//
#
# This source file is part of the waffle open source project
#
# Copyright (c) 2021 KittyBorgX and the waffle project authors
# Licensed under Apache License v2.0 with Runtime Library Exception
#
# See https://github.com/KittyBorgX/waffle/blob/main/LICENSE for license information
# See https://github.com/KittyBorgX/waffle/blob/main/CONTRIBUTORS.md for the list of waffle project contributors
#
# ===----------------------------------------------------------------------===//

import sys

def usage():
    print("")
    print("Waffle's Interpreter!")
    print("")
    print("USAGE: ")
    print("    waffle [OPTIONS] [SUBCOMMAND]")
    print("")
    print("OPTIONS:")
    print("    -h, --help                     Prints help information")
    print("    -v, --version                  Prints the compiler version")
    print("")
    print("SUBCOMMAND:")
    print("    -f, --file [File]              Specify the input file")
    print("    -df, --debug-file [File]       Run the code and debug the file for any errors")
    print("")
    print("OPTIONAL SUBCOMMANDS:")
    print("    -o, --output [File]            Specify the output filename")
    print("")
    print("Example Usage: waffle examples/hello.bf -o hello")

def check_brackets(input_file):
    brackets = 0
    for i in range(len(input_file)):
        if input_file[i] == "[":
            brackets += 1
        elif input_file[i] == "]":
            brackets -= 1
        if brackets < 0:
            print(f"{colors.FAIL}No matching brackets found! Please close the [ bracket at index {i} and check again{colors.ENDC}")
            sys.exit(0)
    if brackets == 0:
        print(f"{colors.OKGREEN}Bracket Matching: True{colors.ENDC}")
        return 0
        # return -1
    else:
        print(f"{colors.FAIL}No matching brackets found! Please close the [ bracket and check again{colors.ENDC}")
        sys.exit(0)

def print_arr_length(array):
    print(f"{colors.OKGREEN}Array Length: {len(array)}{colors.ENDC}")

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
