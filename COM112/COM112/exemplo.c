#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Person{
    char name[20];
    char address[30];
    char phone[20];
} Person;

char *extractToken(const char *const line, char *buffer, size_t bufferLength)
 {
    char  *pointer;
    size_t length;
    if ((line == NULL) || (buffer == NULL))
        return NULL;
    pointer = strpbrk(line, "\t");
    if (pointer == NULL)
        length = strlen(line);
    else
        length = pointer - line;
    if (length >= bufferLength) /* truncate the string if it was too long */
        length = bufferLength - 1;
    buffer[length] = '\0';
    memcpy(buffer, line, length);

    return pointer + 1;
 }

Person parseLineAndExtractPerson(const char *line)
 {
    Person person;

    person.name[0]    = '\0';
    person.address[0] = '\0';
    person.phone[0]   = '\0';

    line = extractToken(line, person.name, sizeof(person.name));
    line = extractToken(line, person.address, sizeof(person.address));
    line = extractToken(line, person.phone, sizeof(person.phone));

    return person;
 }

int main(void)
 {
    char   line[100];
    Person persons[100];
    int    index;
    FILE  *read_file;

    read_file = fopen("arq.txt", "r");
    if (read_file == NULL)
        return -1;
    index = 0;
    while (fgets(line, sizeof(line), read_file) != NULL)
     {
        size_t length;

        length = strlen(line);
        if (line[length - 1] == '\n')
            line[length - 1] = '\0';
        persons[index++] = parseLineAndExtractPerson(line);
     }
    fclose(read_file);
    while (--index >= 0)
        printf("%s: %s, %s\n", persons[index].name, persons[index].address, persons[index].phone);
    return 0;
 }
