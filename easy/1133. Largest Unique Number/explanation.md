# Problem

Given an integer array `nums`, return the largest integer that only occurs once. If no integer occurs once, return `-1`.

 

Example 1:

> **Input:** nums = [5,7,3,9,4,9,8,3,1]\
> **Output:** 8\
> **Explanation:** The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.

Example 2:

> **Input:** nums = [9,9,8,8]\
> **Output:** -1\
> **Explanation:** There is no number that occurs only once.
 

Constraints:

- `1 <= nums.length <= 2000`
- `0 <= nums[i] <= 1000`

# Solution

The goal is to find the largest integer that appears exactly once in the array. If no such integer exists, we return -1.

The solution begins by counting how many times each number appears in the array. This is done using Counter, which creates a frequency map of all elements in nums.

Once we have the frequencies, we iterate through the (number, count) pairs. For each number that occurs exactly once, we compare it with the current maximum unique value and update the answer if it is larger.

If no number with a count of 1 is found during the iteration, the answer remains -1, which correctly represents the case where no unique number exists.

Finally, we return the computed result.

Complexity:
- **Time Complexity:** `O(n)` because we traverse the array once to count elements and once to find the maximum unique number.
- **Space Complexity:** `O(n)` for storing the frequency counts.