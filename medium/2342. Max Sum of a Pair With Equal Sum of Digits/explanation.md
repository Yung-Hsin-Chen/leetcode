# Problem

You are given a **0-indexed** array `nums` consisting of positive integers. You can choose two indices `i` and `j`, such that `i != j`, and the sum of digits of the number `nums[i]` is equal to that of `nums[j]`.

Return the maximum value of `nums[i] + nums[j]` that you can obtain over all possible indices `i` and `j` that satisfy the conditions. If no such pair of indices exists, return `-1`.

 

Example 1:

> **Input:** nums = [18,43,36,13,7]\
> **Output:** 54\
> **Explanation:** The pairs (i, j) that satisfy the conditions are:
> - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
> - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:

> **Input:** nums = [10,12,19,14]\
> **Output:** -1\
> **Explanation:** There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:

- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 109`

# Solution

The goal is to find two different numbers in the array whose sum of digits is equal, and among all such pairs, return the maximum possible sum of the two numbers. If no such pair exists, we return `-1`.

A brute-force approach would compare every pair of numbers and compute their digit sums, which would take `O(n²)` time and be too slow for large inputs. Instead, this solution groups numbers by their digit sums using a hash map.

For each number in nums, we compute its digit sum by converting it to a string and summing its digits. We use a dictionary digit_sums where:
- The key is a digit sum.
- The value is the largest number seen so far with that digit sum.

As we process each number:
 If we have already seen another number with the same digit sum, we can form a valid pair. We compute the candidate sum `num + digit_sums[digit_sum]` and update ans with the maximum value.
- Then, we update `digit_sums[digit_sum]` to store the larger between the current number and the previously stored number. This ensures that for future matches, we always pair with the largest possible number for that digit sum.

By keeping only the maximum number for each digit sum, we efficiently compute the best possible pair.

If no valid pair is found, ans remains `-1`.

### Complexity:
- **Time Complexity:** O(n * d) where d is the number of digits in each number (at most 10), which is effectively O(n).
- **Space Complexity:** O(n) in the worst case if all numbers have distinct digit sums.