# Problem

You are given an integer array `nums`. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

 

Example 1:

> Input: nums = [1,2,3,2]
> Output: 4
> Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:

> Input: nums = [1,1,1,1,1]
> Output: 0
> Explanation: There are no unique elements, and the sum is 0.

Example 3:

> Input: nums = [1,2,3,4,5]
> Output: 15
> Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
 

Constraints:

- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

# Solution

The goal is to compute the sum of all elements that appear exactly once in the array.

A straightforward way to solve this is to first determine how many times each number appears. We use `Counter` to build a frequency map where:
- The key is the number.
- The value is the number of times it appears in `nums`.

Once we have the frequency counts, we iterate through the (number, count) pairs. For each number, if its count is equal to `1`, it is considered unique, and we add it to the running total ans.

If no number appears exactly once, the result naturally remains `0`.

Finally, we return the computed sum.

### Complexity:
- **Time Complexity:** O(n) because we traverse the array once to build the frequency map and once to compute the sum.
- **Space Complexity:** O(n) in the worst case if all elements are distinct.