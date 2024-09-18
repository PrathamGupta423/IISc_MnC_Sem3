#ifndef DICT_H
#define DICT_H

#include "dict_adt.h"

#define DICT_SIZE 100

typedef struct Node {
    struct Node *children;
    int *value;
} Node;

#endif