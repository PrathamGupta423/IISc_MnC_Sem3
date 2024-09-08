# Instructions:
 In this homework, you will reimplement the dictionary (dict.c, dict.h) using a Trie: https://en.wikipedia.org/wiki/Trie. You must modify ONLY these files so that behaviour of the given code (hw2.c) remains exactly the same*** but it executes much faster. Your modified dict must be implemented as a trie and it must implement all the functions in dict_adt.h. You must not include any global variables. (You are free to #define things.)

*** There is ONE exception: The given (naive) dict.c has a hard-coded limit of DICT_SIZE entries. There should be no hard-coded limit in your dictionary. The set function should return 0 only if you cannot allocate additional heap memory.

# Assumptions: 
The key will always be a string of lowercase English letters ('a' to 'z'). The maximum key length is defined in dict_adt.h and the values (id's) are 32-bit ints.

# What to submit: 
A single zip file named as per the SR Numbers of all team members (up to 3) e.g., 20123_20456_20789.zip containing ONLY your modified dict.c and dict.h files.
