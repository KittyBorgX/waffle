#include <stdio.h>
#include "utils.h"

int main(int argc, char *argv[])
{
    int MIN_REQUIRED = 2;
    printf("%d", argc);
    if (argc < MIN_REQUIRED)
    {
        return help();
    }

    return 0;
}