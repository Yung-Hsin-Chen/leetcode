# Problem

Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

 

Example 1:

> **Input:** nums = [10,5,2,6], k = 100\
> **Output:** 8\
> **Explanation:** The 8 subarrays that have product less than 100 are:
> [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]\
> Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

> **Input:** nums = [1,2,3], k = 0\
> **Output:** 0
 

Constraints:

- `1 <= nums.length <= 3 * 104`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 106`

# Solution
This problem can be solved using sliding window since it tries to find number of valid subarrays. The solution is a standard sliding window algorithm. However, one has to be extra careful not only when `k=0` but also `k=1`. In the constraints, it clearly states that the element in `nums` can be `1`. If `k` is also `1`, one might have the `l` pointers moving forward until out of index. For instance, when
> `nums = [1, 1, 1]`\
> `k = 1`

In this example, no matter how much `l` increases, the `curr` will always be 1, and thus keep activating the while loop of increasing `l`. Hence, it is crucial to put `k=1` into the special case at the beginning of the solution.