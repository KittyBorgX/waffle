#!/usr/bin/env python3
import sys

def usage():
    print("")
    print("Waffle's Compiler!")
    print("")
    print("USAGE: ")
    print("    waffle [OPTIONS] [SUBCOMMAND]")
    print("")
    print("OPTIONS:")
    print("    -h, --help                     Prints help information")
    print("    -v, --version                  Prints the compiler version")
    print("")
    print("SUBCOMMAND:")
    print("    -f, --file [Input File]        Specify the input file")
    print("")
    print("OPTIONAL SUBCOMMANDS:")
    print("    -o, --output                   Specify the output filename")
    print("")
    print("Example Usage: waffle examples/hello.bf -o hello")


def main():
    length_args = len(sys.argv)
    # print("Length of args: ", length_args)
    if length_args < 2:
        usage()
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
                print("PLease provide a filename!")
                sys.exit(0)
            else:
                input_filename = sys.argv[2]
                print("The file given is: ", input_filename)
        else:
            print("Invalid option! Use waffle -h to learn about the commands")
            sys.exit(0)


        try:
            with open(input_filename) as f:
                print("File opened successfully")
        except:
            print("Could not open the file!")
            sys.exit(0)

if __name__ == '__main__':
    main()
