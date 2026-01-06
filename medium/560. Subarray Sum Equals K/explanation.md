# Problem

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

> Input: nums = [1,1,1], k = 2\
> Output: 2

Example 2:

> Input: nums = [1,2,3], k = 3\
> Output: 2
 

Constraints:

- `1 <= nums.length <= 2 * 104`
- `-1000 <= nums[i] <= 1000`
- `-107 <= k <= 107`

# Solution

The goal is to count how many contiguous subarrays have a sum equal to `k`.

A brute-force approach would examine all possible subarrays and compute their sums, but this would take `O(n²)` time and is too slow for large inputs. This solution instead uses a prefix sum technique combined with a hash map to achieve linear time complexity.

As we iterate through the array, we maintain a running sum `curr_sum`, which represents the sum of elements from the start of the array up to the current index.

If the sum of a subarray ending at the current index is `k`, then there must exist a previous prefix sum equal to `curr_sum - k`. Therefore, for each position, we check how many times `curr_sum - k` has appeared before and add that count to the answer.

We use a dictionary (prefix_count) to store how many times each prefix sum has occurred. It is initialised with `prefix_count[0] = 1` to handle subarrays that start from index `0`.

For each element:
- Update the running sum.
- Add the number of times `curr_sum - k` has appeared to the result.
- Record the current prefix sum in the dictionary.

By the end of the iteration, ans contains the total number of subarrays whose sum equals `k`.

Complexity:
- Time Complexity: `O(n)` because we traverse the array once.
- Space Complexity: `O(n)` because we store prefix sums in the hash map.