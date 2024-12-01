#include <stdio.h>
#include "dict.h"

int main(int argc, char *argv[]) {
    // Exactly one argument is required: filename
    if (argc != 2) {
        fprintf(stderr, "Usage: %s filename\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");

    // File format is:
    // <int_id>
    // <str_key>
    // <int_id>
    // <str_key>
    // ...
    // 0 (<int_id> is zero)

    Dict d = make_dict();

    while (1) {
        int id;
        char key[MAX_KEY_LENGTH + 1];
        if (fscanf(file, "%d", &id) != 1) {
            break;
        }
        if (id == 0) {
            break;
        }
        fscanf(file, "%s", key);
        int *value = get(d, key);
        if (value == NULL) {
            if (!set(d, key, id)) {
                fprintf(stderr, "Out of memory!\n");  // Should not happen
            }
        } else if (*value < id) {
            *value = id;
        }
    }
    print_dict(d);
    free_dict(d);
    fclose(file);
    return 0;
}