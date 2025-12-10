# Problem

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.

 

Example 1:

> **Input:** nums = [1,2,3,4]\
> **Output:** [1,3,6,10]\
> **Explanation:** Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

> **Input:** nums = [1,1,1,1,1]\
> **Output:** [1,2,3,4,5]\
> **xplanation:** Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
>
Example 3:

> **Input:** nums = [3,1,2,10,1]\
> **Output:** [3,4,6,16,17]

Constraints:

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`

# Solution

This function computes the running sum of an input list `nums`.
A running sum is defined so that each element at index `i` equals the sum of all elements from index `0` to `i`.

The algorithm works as follows:
1. Handle the trivial case:
If the list contains only one element, it is already its own running sum, so the function returns it directly.
2. Initialise the prefix list:
The output list prefix starts with the first element of nums, because the running sum at index `0` is simply that value.
3. Build the running sum iteratively:
For each index `i` from `1` to the end of the list, the algorithm adds the current number `nums[i]` to the previous running sum `prefix[i-1]`, then appends the result to prefix.
This ensures each new element represents the cumulative sum up to that position.
4. Return the result:
Once all positions have been processed, the completed prefix list is returned.

Time and Space Complexity
- **Time complexity:** O(n) — each element is processed once.
- **Space complexity:** O(n) — the output list stores one running sum per input element.
