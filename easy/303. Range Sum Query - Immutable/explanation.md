# Problem

Given an integer array `nums`, handle multiple queries of the following type:

Calculate the sum of the elements of `nums` between indices `left` and `right` inclusive where `left <= right`.

Implement the `NumArray` class:

`NumArray(int[] nums)` Initializes the object with the integer array `nums`.
`int sumRange(int left, int right)` Returns the sum of the elements of `nums` between indices `left` and `right` inclusive (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).
 

Example 1:

> Input: \
> ["NumArray", "sumRange", "sumRange", "sumRange"]\
> [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]\
> Output:\
> [null, 1, -1, -3]\
> Explanation:\
> NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);\
> numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1\
> numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1\
> numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:

- `1 <= nums.length <= 104`
- `-105 <= nums[i] <= 105`
- `0 <= left <= right < nums.length`
- At most `10^4` calls will be made to `sumRange`.

# Solution
The task is to answer many sum-range queries efficiently. A direct approach—adding up elements from left to right every time—would take `O(n)` per query. Since as many as `10,000` queries may occur, repeatedly scanning the array would be too slow. To avoid recomputation, we use a prefix-sum array.

A prefix-sum array stores the cumulative sum of elements from the start of nums up to each index.

For example:

`_prefix[i] = nums[0] + nums[1] + ... + nums[i]`

Once this array is built, we can compute the sum of any subarray in constant time. The sum of `nums[left]` through `nums[right]` is:

`_prefix[right] − _prefix[left] + nums[left]`

This formula works because `_prefix[right]` includes the entire range we want plus everything before left. Subtracting `_prefix[left]` removes the unwanted prefix, but since `_prefix[left]` excludes `nums[left]` itself, we add that single element back.

During initialisation, the class builds the prefix-sum array in a single left-to-right pass. Each call to `sumRange` then returns the requested subarray sum in constant time. This transforms the problem from potentially expensive repeated summing into fast lookups supported by precomputed information.

- **Time Complexity:** O(n) — the prefix-sum array is built with one pass through nums.

- **Space Complexity:** O(n) — storing the prefix-sum array of length equal to the input.