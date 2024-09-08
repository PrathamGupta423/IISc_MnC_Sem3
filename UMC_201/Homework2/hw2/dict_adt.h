#ifndef DICT_ADT_H
#define DICT_ADT_H

// A dictionary for mapping strings to integers
typedef void *Dict;

#define MAX_KEY_LENGTH 100

// Create an empty Dict
Dict make_dict();

// Free up all memory allocated to a Dict (including char* keys)
void free_dict(Dict);

// Get a pointer to the value associated with key
// (returns NULL if no such value exists)
int *get(Dict, const char *key);

// Set the value associated with key to value
// while maintaining insertion order
// (returns 1 if successful, 0 if not)
int set(Dict, const char *key, int value);

// Print the contents of the dictionary
void print_dict(Dict);

#endif