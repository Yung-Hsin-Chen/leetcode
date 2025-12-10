# Problem

Given an array of integers `nums`, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in `nums` (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

 

Example 1:

> **Input:** nums = [-3,2,-3,4,2]\
> **Output:** 5\
> **Explanation:** If you choose startValue = 4, in the third iteration your step by step sum is less than 1.

Example 2:

> **Input:** nums = [1,2]\
> **Output:** 1\
> **Explanation:** Minimum start value should be positive. 

Example 3:

> **Input:** nums = [1,-2,-3]\
> **Output:** 5
 

Constraints:

- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

# Explanation

The running total at each step is equal to startValue + `prefix_sum[i]`, where `prefix_sum[i]` is the sum of the elements from the start of the array up to index `i`. To ensure the running total is never less than 1, the smallest prefix sum must still satisfy:

`startValue + min_prefix_sum ≥ 1`

Rearranging gives:

`startValue ≥ 1 - min_prefix_sum`

but should also satisfy 

`startValue >= 1`

The algorithm therefore scans the array once, keeping a running sum and tracking the smallest value that this running sum reaches. According to the inequality above, we output `1 - min_prefix_sum` as the final answer for startValue. However, if the `startValue <= 1`, the startValue should be `1` instead. Combining the normal cases, and the case that `startValue <= 1`, the final answer should be is `max(1 - min_prefix_sum, 1)`.

- **Time Complexity:** O(n) because the algorithm scans the array once while maintaining a running sum and tracking the minimum prefix sum, so the total work grows linearly with the number of elements.
- **Space Complexity:** O(1) because only a few variables are used to store the running sum and minimum prefix sum, so the memory required does not increase with the input size.