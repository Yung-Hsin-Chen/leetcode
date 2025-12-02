# Problem

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

> **Input:** nums = [-4,-1,0,3,10]\
> **Output:** [0,1,9,16,100]\
> **Explanation:** After squaring, the array becomes [16,1,0,9,100].
> After sorting, it becomes [0,1,9,16,100].

Example 2:

> **Input:** nums = [-7,-3,2,3,11]\
> **Output:** [4,9,9,49,121]
 

Constraints:

- `1 <= nums.length <= 104`
- `-104 <= nums[i] <= 104`
- `nums` is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

# Solution

This problem can be solved using two pointers, `l` and `r`. We first pre-define an array `ans` with length `nums`, and start filling this array from the right. We take the larger value after squared of the two pointers, and put it into the right most unfilled space in `ans`. Repeat this until the two pointers have go through all the elements in `nums`.

The time complexity of this solution is `O(n)`, and the space complexity is `O(n)`.