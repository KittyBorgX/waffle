#!/usr/bin/env python3

# ===----------------- waffle.py - Core file of the waffle project ------------===//
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
import threading
from utils import usage, check_brackets, print_arr_length, colours
from interpreter import interpret

WAFFLE_VERSION = "0.1.0"


def repl() -> None:
    try:
        print(f"{colours.CYAN}Waffle Interpreter, Version {WAFFLE_VERSION} {colours.END_COLOUR}")
        print(f"Use {colours.GREEN}Ctrl + C{colours.END_COLOUR} Key Combination to quit out of the REPL")
        print(f"Use {colours.GREEN}waffle --help{colours.END_COLOUR} to learn more\n")
        while True:
            try:
                repl_input = input(">> ")
                try:
                    interpret(repl_input, len(repl_input))
                except:
                    out = exec(repl_input)
                    if out != None:
                        print(f"\n{out}")
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt as e:
        print("\nExiting...")

def main():
    debugging = False
    length_args = len(sys.argv)
    # print("Length of args: ", length_args)
    if length_args < 2:
        # usage()
        repl()
        sys.exit(0)

    else:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            usage()
            sys.exit(0)
        elif sys.argv[1] == '-v' or sys.argv[1] == '--version':
            print(f'{WAFFLE_VERSION}')
            sys.exit(0)

        elif sys.argv[1] == '-f' or sys.argv[1] == '--file':
            if length_args == 2:
                print("Please provide a filename!")
                sys.exit(0)
            else:
                input_filename = sys.argv[2]


        elif sys.argv[1] == '-df' or sys.argv[1] == '--debug-file':
            if length_args == 2:
                print("Please provide a filename!")
                sys.exit(0)
            else:
                input_filename = sys.argv[2]
                debugging = True


        else:
            print("Invalid option! Use waffle -h to learn about the commands")
            sys.exit(0)


        try:
            with open(input_filename) as f:
                contents = f.read()
                if debugging:
                    # check_brackets(contents)
                    # print_arr_length(contents)
                    # interpret(contents, len(contents))
                    check_brackets_thread = threading.Thread(target=check_brackets, args=(contents,))
                    print_arr_length_thread = threading.Thread(target=print_arr_length, args=(contents,))
                    interpret_thread = threading.Thread(target=interpret, args=(contents, len(contents)))

                    check_brackets_thread.start()
                    print_arr_length_thread.start()
                    interpret_thread.start()

                else:
                    # interpret(contents, len(contents))
                    interpret_thread = threading.Thread(target=interpret, args=(contents, len(contents)))
                    interpret_thread.start()


        except FileNotFoundError:
            print("Could not find the specified file!")
            sys.exit(0)

if __name__ == '__main__':
    main()
