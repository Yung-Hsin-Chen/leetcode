# Problem

You are given an integer array nums consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose length is equal to `k `that has the maximum average value and return this value. Any answer with a calculation error less than `10^{-5}` will be accepted.

 

Example 1:

> **Input:** nums = [1,12,-5,-6,50,3], k = 4\
> **Output:** 12.75000\
> **Explanation:** Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

> **Input:** nums = [5], k = 1\
> **Output:** 5.00000
 

Constraints:

- `n == nums.length`
- `1 <= k <= n <= 105`
- `-104 <= nums[i] <= 104`

# Solution
Since the problem is asking for a fixed length subarray, this can be solved using sliding window. The problem is asking for the average. However, it is sufficient to compare just the sum of the context window, and then divide the sum by `k` in the output.

The time complexity is `O(n)`, while the space complexity is `O(1)`.