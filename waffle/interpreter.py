# ===----------------- interpreter.py - Interpretting bf code ----------------===//
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

def interpret(code, arr_length):
    # initialize variables
    data = [0] * arr_length
    ptr = 0
    code_ptr = 0
    while code_ptr < len(code):
        # increment data pointer
        if code[code_ptr] == '>':
            ptr += 1
            if ptr == len(data):
                data.append(0)
        # decrement data pointer
        elif code[code_ptr] == '<':
            ptr -= 1
        # increment data
        elif code[code_ptr] == '+':
            data[ptr] += 1
        # decrement data
        elif code[code_ptr] == '-':
            data[ptr] -= 1
        # output data
        elif code[code_ptr] == '.':
            print(chr(data[ptr]), end='')
        # input data
        elif code[code_ptr] == ',':
            data[ptr] = ord(input())
        # jump forward
        elif code[code_ptr] == '[':
            if data[ptr] == 0:
                while code[code_ptr] != ']':
                    code_ptr += 1
                # Check if there is no closing ] for the opening [

        # jump backward
        elif code[code_ptr] == ']':
            if data[ptr] != 0:
                while code[code_ptr] != '[':
                    code_ptr -= 1
        # increment code pointer
        code_ptr += 1
