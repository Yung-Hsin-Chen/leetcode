# Problem

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is unique or `false` otherwise.

Example 1:

> Input: arr = [1,2,2,1,1,3]\
> Output: true\
> Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

> Input: arr = [1,2]\
> Output: false

Example 3:

> Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]\
> Output: true
 

Constraints:

- `1 <= arr.length <= 1000`
- `-1000 <= arr[i] <= 1000`

# Solution

The goal is to determine whether the frequency of each distinct number in the array is unique. In other words, no two different values should appear the same number of times.

First, we use Counter to count how many times each number appears in `arr`. This produces a frequency map where:
- The key is the number.
- The value is its number of occurrences.

Next, we extract all frequency values using `counts.values()`. If two different numbers share the same frequency, then those frequency values will contain duplicates.

To check uniqueness, we convert the frequencies into a set. Since a set removes duplicates, we compare:
- The number of distinct frequencies: `len(set(counts.values()))`
- The number of distinct numbers: `len(counts)`

If these two lengths are equal, it means every frequency was unique, so we return `True`. Otherwise, at least two numbers share the same occurrence count, and we return `False`.

### Complexity:
- **Time Complexity:** O(n) because we traverse the array once to build the frequency map and perform set operations on at most n values.
- **Space Complexity:** O(n) in the worst case if all elements are distinct.