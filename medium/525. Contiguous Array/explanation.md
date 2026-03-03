# Problem

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

# Solution

The goal is to find the maximum length of a contiguous subarray that contains an equal number of `0` and `1`.

A brute-force approach would check every possible subarray and count how many `0`s and `1`s it contains, but this would take `O(n²)` time and is too slow for nums.length up to `10^5`. This solution uses a prefix-sum style method with a hash map to achieve `O(n)` time.

The key idea is to convert the problem into tracking a running “balance” between ones and zeros. We treat each `1` as `+1` and each `0` as `-1`. Then, for any subarray, having equal numbers of `0` and `1` means the total balance of that subarray is `0`.

We maintain a running value prefix, which is the balance from the start of the array up to the current index. If the same prefix value occurs at two different indices, it means the balance between those indices is zero, so the subarray between them contains equal numbers of `0` and `1`.

To maximise the length, we store in counts the first index where each prefix value appeared. When we see the same prefix again at index `i`, the subarray from `counts[prefix] + 1` to `i` is balanced, and its length is `i - counts[prefix]`. We update the answer with the maximum such length.

We initialise `counts[0] = -1` to represent that a balance of 0 occurs before the array starts. This allows subarrays starting at index `0` to be counted correctly.

By scanning the array once and using the hash map to find the earliest occurrence of each balance value, we compute the longest balanced subarray efficiently.

- **Time complexity:** O(n) because we traverse the array once and hash map operations are constant time on average.
- **Space complexity:** O(n) because we may store an entry for many distinct prefix values.