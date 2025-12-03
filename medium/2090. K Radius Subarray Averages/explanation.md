# Problem

You are given a 0-indexed array `nums` of `n` integers, and an integer `k`.

The k-radius average for a subarray of nums centered at some index `i` with the radius `k` is the average of all elements in `nums` between the indices `i - k` and `i + k` (inclusive). If there are less than `k` elements before or after the index `i`, then the k-radius average is `-1`.

Build and return an array `avgs` of length `n` where `avgs[i]` is the k-radius average for the subarray centered at index `i`.

The average of `x` elements is the sum of the `x` elements divided by `x`, using integer division. The integer division truncates toward zero, which means losing its fractional part.

- For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

Example 1:
> **Input:** nums = [7,4,3,9,1,8,5,2,6], k = 3\
> **Output:** [-1,-1,-1,5,4,4,-1,-1,-1]\
> **Explanation:**
> - avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
> - The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.\
> Using integer division, avg[3] = 37 / 7 = 5.
> - For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
> - For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
> - avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.

Example 2:

> **Input:** nums = [100000], k = 0\
> **Output:** [100000]\
> **Explanation:**
> The sum of the subarray centered at index 0 with radius 0 is: 100000.\
> avg[0] = 100000 / 1 = 100000.

Example 3:

> **Input:** nums = [8], k = 100000\
> **Output:** [-1]\
> **Explanation:** 
> avg[0] is -1 because there are less than k elements before and after index 0.

Constraints:

- `n == nums.length`
- `1 <= n <= 105`
- `0 <= nums[i], k <= 105`

# Explanation

The problem asks for the k-radius average at each index. An index `i` is valid only if it has at least `k` elements before it and at least `k` elements after it. That means each valid window has length `2k + 1`. If there are not enough elements on either side, the result for that index is `-1`.

The code first handles two simple cases:
	1.	If the array is shorter than `2k + 1`, then no index has enough elements on both sides, so the result is an array of -1.
	2.	If `k == 0`, the radius is zero, so the k-radius average at index `i` is simply `nums[i]`.

For the general case, the solution constructs a prefix-sum array. `prefix[i]` contains the sum of all elements from index `0` to `i`. This allows the sum of any subarray `[l, r]` to be computed in constant time using:

`prefix[r] - prefix[l - 1]`

(with `prefix[r]` alone when `l == 0`).

Using the prefix sums, the code iterates through all indices and overwrites `nums[i]` with its k-radius average:
	•	When `i == k`, the window starts at index `0`, so the sum is simply `prefix[i + k]`.
	•	For all `i` such that `k + 1 <= i < len(nums) - k`, it computes the window sum using
`prefix[i + k] - prefix[i - k - 1]`.
	•	All other indices cannot form a full window, so they are set to `-1`.

Every valid window sum is divided by `(2k + 1)` using integer division, as required.

- **Time Complexity:** O(n) , because both the prefix construction and the averaging loop scan the array once.
- **Space Complexity:** O(n), due to storing the prefix-sum array.