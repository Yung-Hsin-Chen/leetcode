# Problem

Given an array of integers `nums` and an integer `k`. A continuous subarray is called nice if there are `k` odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

> Input: nums = [1,1,2,1,1], k = 3\
> Output: 2\
> Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

> Input: nums = [2,4,6], k = 1\
> Output: 0\
> Explanation: There are no odd numbers in the array.

Example 3:

> Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2\
> Output: 16
 

Constraints:

- `1 <= nums.length <= 50000`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= nums.length`

# Solution

The goal is to count how many contiguous subarrays contain exactly `k` odd numbers. Such subarrays are called nice.

A brute-force approach would examine all possible subarrays and count the odd numbers in each one, but this would take `O(n²)` time and is too slow for large inputs. Instead, this solution uses a prefix-counting technique to achieve linear time complexity.

We iterate through the array while keeping track of how many odd numbers we have seen so far. For each position, we maintain `curr_odd`, which represents the total number of odd elements from the start of the array up to the current index.

If a subarray ending at the current index contains exactly `k` odd numbers, then there must exist a previous prefix where the number of odd elements was `curr_odd - k`. Therefore, for each step, we count how many times `curr_odd - k` has appeared before and add that to the answer.

A dictionary (counts) is used to store how many times each prefix odd-count has occurred. It is initialised with `counts[0] = 1` to handle subarrays that start at index `0`.

For each number in the array:
- Update `curr_odd` by adding `1` if the number is odd.
- Add `counts[curr_odd - k]` to the result.
- Increment the count of the current `curr_odd`.

By the end of the iteration, ans contains the total number of nice subarrays.

Complexity:
- **Time Complexity:** `O(n)` because we traverse the array once.
- **Space Complexity:** `O(n)` because we store prefix odd counts in the hash map.