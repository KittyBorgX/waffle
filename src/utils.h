#include <stdio.h>

int help()
{
    printf("\nPancake VM!\n\n");
    printf("USAGE: \n");
    printf("    pancake [OPTIONS] [SUBCOMMAND]\n\n");
    printf("OPTIONS:\n");
    printf("    -h, --help                     Prints help information\n");
    printf("    -v, --version                  Prints the compiler version\n\n");
    printf("SUBCOMMAND:\n");
    printf("    -f, --file [File]              Specify the input file\n");
    printf("    -df, --debug-file [File]       Run the code and debug the file for any errors\n\n");
    printf("OPTIONAL SUBCOMMANDS:\n");
    printf("    -o, --output [File]            Specify the output filename\n\n");
    printf("Example Usage: waffle examples/hello.bf -o hello\n\n");
    return 0;
}