#ifndef DICT_H
#define DICT_H

#include "dict_adt.h"

#define DICT_SIZE 100

typedef struct dict_entry {
    char *key;
    int value;
} dict_entry;

typedef struct array_dict {
    dict_entry entries[DICT_SIZE];
    int size;
} array_dict;

#endif