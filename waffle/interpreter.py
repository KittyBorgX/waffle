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
