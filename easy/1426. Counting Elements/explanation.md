# Problem

Given an integer array `arr`, count how many elements `x` there are, such that `x + 1` is also in `arr`. If there are duplicates in `arr`, count them separately.

 

Example 1:

> Input: arr = [1,2,3]\
> Output: 2\
> Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Example 2:

> Input: arr = [1,1,3,3,5,5,7,7]\
> Output: 0\
> Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
 

Constraints:

- `1 <= arr.length <= 1000`
- `0 <= arr[i] <= 1000`

# Solution

The goal is to count how many elements `x` in the array satisfy the condition that `x + 1` is also present in the array. If a value appears multiple times, each occurrence is counted separately.

A brute-force approach would check, for every element, whether `x + 1` exists by scanning the array. This would lead to `O(n²)` time complexity, which is unnecessary given the constraints.

This solution improves efficiency by using a set.

First, we convert the array into a set. This allows us to check whether a value exists in constant time, `O(1)`.

We then iterate through the original array (not the set). For each number num, we check whether `num + 1` exists in the set. If it does, we increment the counter.

Iterating over the original array is important because duplicates must be counted separately. Even if the set removes duplicates, each occurrence in the array is still evaluated individually.

Finally, we return the total count.

Complexity:
- **Time Complexity:** `O(n)` because we iterate through the array once and set lookups are constant time on average.
- **Space Complexity:** `O(n)` because we store the elements of the array in a set.