#include <stdio.h>

void colour_red()
{
    printf("\033[91m");
}

void colour_yellow()
{
    printf("\033[93m");
}

void colour_blue()
{
    printf("\033[94m");
}

void colour_cyan()
{
    printf("\033[96m");
}

void colour_green()
{
    printf("\033[92m");
}

void reset()
{
    printf("\033[0m");
}
