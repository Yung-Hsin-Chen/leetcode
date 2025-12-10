# Problem

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

Example 1:

> **Input:** target = 7, nums = [2,3,1,2,4,3]\
> **Output:** 2\
> **Explanation:** The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

> **Input:** target = 4, nums = [1,4,4]\
> **Output:** 1\

Example 3:

> **Input:** target = 11, nums = [1,1,1,1,1,1,1,1]\
> **Output:** 0
 

Constraints:

- `1 <= target <= 109`
- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 104`
  
# Solution

The key idea is that every number in the array is positive. That means the sum of a window only increases when we extend it and only decreases when we shrink it. This predictable behaviour lets us use a sliding window rather than checking all possible subarrays.

Imagine you place a left pointer at the start of the array and begin expanding the window to the right. As you include more numbers, the running total slowly grows. Whenever the total finally reaches or exceeds the target, you know two things: the current window is valid, and it might be possible to make it shorter by trimming numbers from its left side. Because the numbers are positive, removing elements from the left can only reduce the sum, never increase it, so this trimming lets you find the shortest valid window ending at that position.

The process then becomes rhythmic: expand to the right until the sum is large enough, then shrink from the left until shrinking any further would make the sum too small. Each time the window is valid, record its length. Continue this pattern until the right pointer reaches the end of the array. If no window ever reaches the target, the answer is zero; otherwise, the answer is the shortest window you found.

This works efficiently because each pointer only moves forward. The right pointer walks through the array once, and the left pointer also walks forward at most once. Even though there is a loop inside a loop, the total movement across the array is linear rather than quadratic.

**Attention:**\
 In many sliding-window problems we do shrink the window when it becomes invalid.
Here, the twist is that validity flips direction, because we want the minimum window length, not the maximum.

- If you’re asked for the longest window with a constraint, shrink when invalid.
- If you’re asked for the shortest window with a constraint, shrink when valid.

This principle explains almost every sliding window pattern.

- **Time complexity:** O(n)
- **Space complexity:** O(1)