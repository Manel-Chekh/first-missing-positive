# First Missing Positive

Returns the smallest positive integer (n > 0) that is not present in an unsorted array.

Example: [0, -2, 1, 2] -> 3

## Approach
The answer is always between 1 and len(nums) + 1. Put the numbers in a set, then test 1, 2, 3... until one is missing. Time O(n), memory O(n).

## Run
    python solution.py
