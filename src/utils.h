#include <stdio.h>
#include "colours.h"

int help()
{
    colour_blue();
    printf("\nwaffle VM!\n\n");
    reset();
    colour_cyan();
    printf("USAGE: \n");
    reset();
    colour_green();
    printf("    waffle [OPTIONS] [SUBCOMMAND]\n\n");
    reset();
    colour_cyan();
    printf("OPTIONS:\n");
    reset();
    colour_green();
    printf("    -h, --help                     Prints help information\n");
    printf("    -v, --version                  Prints the compiler version\n\n");
    reset();
    colour_cyan();
    printf("SUBCOMMAND:\n");
    reset();
    colour_green();
    printf("    -f, --file [File]              Specify the input file\n");
    printf("    -df, --debug-file [File]       Run the code and debug the file for any errors\n\n");
    reset();
    colour_cyan();
    printf("OPTIONAL SUBCOMMANDS:\n");
    reset();
    colour_green();
    printf("    -o, --output [File]            Specify the output filename\n\n");
    reset();
    colour_yellow();
    printf("Example Usage: waffle examples/hello.bf -o hello\n\n");
    reset();
    return 0;
}
