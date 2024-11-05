# Problem Statement

Your friend wants a suitable data structure for the following task involving `n` distinct numbers.

## Task Description

1. **Step 1**: The `n` numbers will be provided (in some random order) and should be stored in the data structure.
2. **Step 2**: A series of `m` queries (`m` much larger than `n`) will be performed, where at least `c.m` of these queries will be for one of the numbers `x` provided in Step 1. (Here, `0 < c < 1` is a constant, independent of `n`).

The required data structure must ensure that the amortized cost of each search for `x` is `O(1)`, where the hidden constant can depend on `c`.

## Objective

Your task is to experimentally convince your friend that splay trees can be an appropriate data structure. (Note: There is a theoretical justification, but your friend does not understand the maths involved!)

## Implementation

You can use this [Java implementation of splay trees](https://github.com/TheAlgorithms/Java/blob/master/src/main/java/com/thealgorithms/datastructures/trees/SplayTree.java) as a starting point. Your whole assignment can be in Java, if you like. Alternatively, you can translate that implementation into another language (e.g., Python) -- if you do this, consider contributing it to the GitHub repo linked above.

## Evaluation

For evaluation, our TAs will be "your friend" -- you will have to convince them on Fri Nov 8.

## Steps to Follow

1. **Implement the Splay Tree**: Start with the provided Java implementation or translate it into another language.
2. **Store the Numbers**: Implement the functionality to store `n` distinct numbers in the splay tree.
3. **Perform Queries**: Implement the functionality to perform `m` queries and ensure that at least `c.m` of these queries are for one of the numbers `x`.
4. **Experimental Analysis**: Conduct experiments to show that the amortized cost of each search for `x` is `O(1)`.
5. **Documentation**: Document your implementation, experiments, and results to convince your friend (the TAs).

Good luck!