#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "dict.h"

// Create an empty Dict
Dict make_dict() {
    array_dict *dict = (array_dict *) malloc(sizeof(array_dict));
    if (dict == NULL) {
        return NULL;
    }
    dict->size = 0;
    return (Dict) dict;
}

// Free up all memory allocated to a Dict (including char* keys)
void free_dict(Dict dict_adt) {
    if (dict_adt != NULL) {
        array_dict *dict = (array_dict *) dict_adt;
        for (int i = 0; i < dict->size; i++) {
            char *key = dict->entries[i].key;
            if (key != NULL) {
                free(key);
            }
        }
    }
}

// Get a pointer to the value associated with key
// (returns NULL if no such value exists)
int *get(Dict dict_adt, const char *key) {
    if (dict_adt == NULL) {
        return NULL;
    }
    array_dict *dict = (array_dict *) dict_adt;
    for (int i = 0; i < dict->size; i++) {
        if (strcmp(dict->entries[i].key, key) == 0) {
            return &(dict->entries[i].value);
        }
    }
    return NULL;
}

// Set the value associated with key to value
// while maintaining insertion order
// (returns 1 if successful, 0 if not)
int set(Dict dict_adt, const char *key, int value) {
    if (dict_adt == NULL) {
        return 0;
    }
    array_dict *dict = (array_dict *) dict_adt;
    int i = 0;
    for (; i < dict->size; i++) {
        int cmp = strcmp(dict->entries[i].key, key);
        if (cmp == 0) {
            dict->entries[i].value = value;
            return 1;
        } else if (cmp > 0) {
            break;
        }
    }
    if (dict->size == DICT_SIZE) {
        return 0;
    }
    for (int j = dict->size; j > i; j--) {
        dict->entries[j] = dict->entries[j - 1];
    }
    dict->entries[i].key = strdup(key);
    if (dict->entries[i].key == NULL) {
        return 0;
    }
    dict->entries[i].value = value;
    dict->size++;
    return 1;
}

// Print the contents of the dictionary
void print_dict(Dict dict_adt) {
    if (dict_adt == NULL) {
        return;
    }
    array_dict *dict = (array_dict *) dict_adt;
    for (int i = 0; i < dict->size; i++) {
        printf("%s: %d\n", dict->entries[i].key, dict->entries[i].value);
    }
}