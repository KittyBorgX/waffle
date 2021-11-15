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
from utils import usage, check_brackets, print_arr_length, colors
from interpreter import interpret

def repl() -> None:
    try:
        while True:
            try:
                repl_input = input(">> ")
                try:
                    interpret(repl_input, len(repl_input))
                except:
                    out = exec(repl_input)
                    if out != None:
                        print(out)
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
            print('Waffle v0.1')
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
                    check_brackets(contents)
                    print_arr_length(contents)
                    interpret(contents, len(contents))
                else:
                    interpret(contents, len(contents))


        except FileNotFoundError:
            print("Could not find the specified file!")
            sys.exit(0)

if __name__ == '__main__':
    main()
