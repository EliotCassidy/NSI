#include <stdio.h>
#include <string.h>
#include <ctype.h>
char* palindrome(char* text);

int main(void)
{
    printf(palindrome("Kayak"));
}

char* palindrome(char* text)
{
    int min = 0;
    int max = strlen(text);
    while (min < max)
    {
        if (!isalnum(text[min]))
        {
            min++;
            continue;
        }
        if (!isalnum(text[max-1]))
        {
            max--;
            continue;
        }
        if (tolower(text[min]) != tolower(text[max-1]))
        {
            return "false\n";
        }
        min++;
        max--;
    }
    return "true\n";
}