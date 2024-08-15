# Modify this file to implement the count_pairs_file function
# using ultra-large integers in C/C++.

import time # For performance measurement

import ctypes
from ctypes import c_char_p, c_int

# Load the shared library
lib = ctypes.CDLL('./libarbit.so')

# Define the function prototype
lib.count_pairs_file_c.argtypes = [c_char_p]
lib.count_pairs_file_c.restype = ctypes.c_longlong

def read_file(filename: str) -> tuple[list[int], int]:
    with open(filename) as file:
        # First line is the target
        target = int(file.readline())
        # Second line is the number of integers
        n = int(file.readline())
        # Read the n integers and return them as a list
        return ([int(file.readline()) for _ in range(n)], target)


def count_pairs(data: list[int], target: int) -> int:
    """Count the number of pairs of
    list indices i < j such that
    data[i] - data[j] = target.
    Time complexity: Naive O(n^2).
    """
    result = 0
    n = len(data)
    # completion = 0
    # total = n * (n - 1) / 2
    for i in range(n - 1):
        for j in range(i + 1, n):
            if data[i] - data[j] == target:
                result += 1 
        # if(i % (n/1000) == 0): # Print progress every 100 iterations
            # print(f"Completion: {i/n * 100:.2f}%") # Print progress 

            
    return result


def test_count_pairs():
    # Simple correctness tests
    assert count_pairs([1, 2, 3, 4, 5], 1) == 0
    assert count_pairs([5, 4, 3, 2, 1], 1) == 4
    assert count_pairs([1, 2, 3, 4, 5], -3) == 2
    # Test with huge integers
    assert count_pairs([10**20 + 2, 10**20 + 1, 10**20], 1) == 2
    print("count_pairs.py: All tests passed")


def count_pairs_file(filename: str) -> int:


    # Temporary Code for testing
    start_python = time.time()
    data, target = read_file(filename)
    py =  count_pairs(data, target)
    end_python = time.time()
    print(f"Python time with logging: {end_python - start_python}")

    start_c = time.time()
    c = lib.count_pairs_file_c(filename.encode('utf-8'))
    end_c = time.time()
    print(f"C time: {end_c - start_c}")

    assert py == c

    return c
    #

    #Final Code
    #return lib.count_pairs_file_c(filename.encode('utf-8'))

def test_python_implementation(filename: str) -> (int, float):
    start_python = time.time()
    data, target = read_file(filename)
    py =  count_pairs(data, target)
    end_python = time.time()
    return py, end_python - start_python

def test_c_implementation(filename: str) -> (int, float):
    start_c = time.time()
    c = lib.count_pairs_file_c(filename.encode('utf-8'))
    end_c = time.time()
    return c, end_c - start_c


