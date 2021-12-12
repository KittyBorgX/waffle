# ===----------------- utils.py - Functions for output and colours -------------===//
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
    print(f"{colours.BLUE}Waffle Interpreter!{colours.END_COLOUR}")
    print("")
    print(f"{colours.CYAN}USAGE: {colours.END_COLOUR}")
    print(f"{colours.GREEN}    waffle [OPTIONS] [SUBCOMMAND]{colours.END_COLOUR}")
    print("")
    print(f"{colours.CYAN}OPTIONS:{colours.END_COLOUR}")
    print(f"{colours.GREEN}    -h, --help                     Prints help information{colours.END_COLOUR}")
    print(f"{colours.GREEN}    -v, --version                  Prints the compiler version{colours.END_COLOUR}")
    print("")
    print(f"{colours.CYAN}SUBCOMMAND:")
    print(f"{colours.GREEN}    -f, --file [File]              Specify the input file{colours.END_COLOUR}")
    print(f"{colours.GREEN}    -df, --debug-file [File]       Run the code and debug the file for any errors{colours.END_COLOUR}")
    print("")
    print(f"{colours.CYAN}OPTIONAL SUBCOMMANDS:{colours.END_COLOUR}")
    print(f"{colours.GREEN}    -o, --output [File]            Specify the output filename{colours.END_COLOUR}")
    print("")
    print(f"{colours.YELLOW}Example Usage: waffle examples/helloworld.bf -o hello{colours.END_COLOUR}")
    print("")

def check_brackets(input_file):
    brackets = 0
    for i in range(len(input_file)):
        if input_file[i] == "[":
            brackets += 1
        elif input_file[i] == "]":
            brackets -= 1
        if brackets < 0:
            print(f"{colours.RED}No matching brackets found! Please close the [ bracket at index {i} and check again{colours.END_COLOUR}")
            sys.exit(0)
    if brackets == 0:
        print(f"{colours.GREEN}Bracket Matching: True{colours.END_COLOUR}")
        return 0
        # return -1
    else:
        print(f"{colours.RED}No matching brackets found! Please close the [ bracket and check again{colours.END_COLOUR}")
        sys.exit(0)

def print_arr_length(array):
    print(f"{colours.GREEN}Array Length: {len(array)}{colours.END_COLOUR}")

class colours:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END_COLOUR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
