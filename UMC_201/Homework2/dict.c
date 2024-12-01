#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "dict.h"

void dfs(Node *, char *, int count);
void _private_free_dict(Dict);

// Create an empty Dict
Dict make_dict() {
    Node *root = (Node *) malloc(sizeof(Node));
    if (root == NULL) {
        return NULL;
    }
    root->children = NULL;
    root->value = NULL;
    return (Dict) root;
}

// Get a pointer to the value associated with key
// (returns NULL if no such value exists)
int *get(Dict dict, const char *key) {
    if (dict == NULL){
        return NULL;
    }
    int i = 0;
    Node *diction = (Node *)dict;
    Node *child = diction->children;
    Node *parent = diction;
    while (key[i] != 0) {
        if (child != NULL){
            parent = child+(key[i] - 97);
            child = (child+(key[i] - 97))->children;
            i++;
        }
        else{
            return NULL;
        }
    }
    return parent->value;
}

// Set the value associated with key to value
// while maintaining insertion order
// (returns 1 if successful, 0 if not)
int set(Dict dict_adt, const char *key, int valued) {
    if (dict_adt == NULL) {
        return 0;
    }
    int i = 0;
    Node *diction = (Node *)dict_adt;
    Node *child = diction->children;
    Node *parent = diction;
    while (key[i] != 0) {
        if (child != NULL){
            parent = child+(key[i] - 97);
            child = (child+(key[i] - 97))->children;
            i++;
        }
        else{
            child = (Node *)malloc(26*sizeof(Node));
            parent->children = child;
            if (child == NULL)
            {
                printf("ERROR\n");
                return 0;
            }
            for (int j = 0; j < 26; j++){
                child[j].children = NULL;
                child[j].value = NULL;
            }
            parent = child+(key[i] - 97);
            child = (child+(key[i] - 97))->children;
            i++;
        }
    }
    parent->value = (int *)malloc(sizeof(int));
    *(parent->value) = valued;
    return 1;
}



// Print the contents of the dictionary
void print_dict(Dict dict_adt) {
    if (dict_adt == NULL) {
        return;
    }
    char *key = (char *)malloc(101);
    dfs((Node *)dict_adt, key, 0);
    //print the value for key abc
    free(key);
}

void dfs(Node *diction, char *key, int count) {
    //also print the key
    if (diction->value != NULL){
        int i = 0;
        key[count] = 0;
        printf("%s", key);
        printf(": %d\n", *(diction->value));
    }
    if (diction->children == NULL){
        return;
    }
    for (int i = 0; i < 26; i++){
            key[count] = i+'a';
            dfs((diction->children)+i, key, count+1);
            key[count] = 0;
    }
}

// Free up all memory allocated to a Dict (including char* keys)
void free_dict(Dict dict_adt) {
    if (dict_adt == NULL) {
        return;
    }

    _private_free_dict(dict_adt);
    Node *diction = (Node *)dict_adt;
    free (diction);


}



void _private_free_dict(Dict dict_adt) {
    if (dict_adt == NULL) {
        return;
    }
    Node *diction = (Node *)dict_adt;
    if(diction->value != NULL){
        free(diction->value);
    }
    if (diction->children != NULL){
        for(int i = 0; i < 26; i++){
            _private_free_dict((diction->children)+i);
        }
        free(diction->children);
    }
}