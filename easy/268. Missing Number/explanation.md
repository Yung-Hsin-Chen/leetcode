# Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

 

Example 1:

> **Input:** nums = [3,0,1]\
> **Output:** 2\
> **Explanation:** `n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. `2` is the missing number in the range since it does not appear in nums.

Example 2:

> **Input:** nums = [0,1]\
> **Output:** 2\
> **Explanation:** `n = 2` since there are 2 numbers, so all numbers are in the range `[0,2]`. `2` is the missing number in the range since it does not appear in nums.

Example 3:
> **Input:** nums = [9,6,4,2,3,5,7,0,1]\
> **Output:** 8\
> **Explanation:** `n = 9` since there are 9 numbers, so all numbers are in the range `[0,9]`. `8` is the missing number in the range since it does not appear in nums.

Constraints:

- n == nums.length
- 1 <= n <= 104
- 0 <= nums[i] <= n
- All the numbers of nums are unique.
 

Follow up: Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

# Solution

The goal is to find the one missing number from an array containing `n` distinct numbers taken from the range `[0, n]`. Since exactly one number in this range is missing, we need to identify which value does not appear in the array.

This solution takes advantage of the fact that, after sorting, a correctly filled array should have the value `i` at index `i`.

First, we sort the array. After sorting, if no number were missing, the array would look like:

```
[0, 1, 2, 3, ..., n]
```
We then iterate through the array and compare each element with its index. At the first position where `nums[i] != i`, we know that `i` is the missing number, because every number before it matches the expected pattern.

If the loop finishes without finding a mismatch, it means all numbers from `0` to `n-1` are present, and therefore the missing number must be `n`. This is why we return `i + 1` after the loop.

This approach is simple and easy to understand, though it does not meet the follow-up requirement due to sorting.

Complexity:
- **Time Complexity:** `O(n log n)` because sorting the array dominates the runtime.
- **Space Complexity:** `O(1)` extra space (ignoring the space used by the sorting algorithm because we sorted `nums` in place).