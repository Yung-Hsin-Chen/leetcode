# Problem

Given an array of integers `nums`, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return `-1`.

 

Example 1:

> Input: nums = [1,7,3,6,5,6]\
> Output: 3\
> Explanation:
> The pivot index is 3.
> Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
> Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

> Input: nums = [1,2,3]\
> Output: -1\
> Explanation:
> There is no index that satisfies the conditions in the problem statement.

Example 3:

> Input: nums = [2,1,-1]\
> Output: 0\
> Explanation:
> The pivot index is 0.
> Left sum = 0 (no elements to the left of index 0)
> Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

- `1 <= nums.length <= 104`
- `-1000 <= nums[i] <= 1000`

# Solution
The pivot index is the position in the array where the sum of all elements to the left equals the sum of all elements to the right. To find such an index efficiently, we avoid recomputing sums for every position by using prefix sums.

A prefix sum array stores the cumulative sum up to each index.
For example, if `prefix[i]` represents the sum of `nums[0]` through `nums[i]`, then:
- the left sum at index `i` is
`prefix[i] − nums[i]`
because it excludes the current element;
- the right sum at index i is
`prefix[-1] − prefix[i]`
since it subtracts everything up to and including index `i` from the total sum.

After building the prefix sum array, we simply scan through the indices one by one. For each index, we compute the left and right sums using the prefix values. The first time these two sums match, we have found the leftmost pivot index and return it. If no index satisfies the condition, the answer is `-1`.

This approach ensures that each sum comparison is done in constant time, and no repetitive summing is required.

- **Time Complexity:** O(n) - Building the prefix sum array takes one pass through the list, and checking each index takes another pass. Both steps together still run in linear time.

- **Space Complexity:** O(n) - We store a prefix sum array of the same length as the input, requiring additional space proportional to n.
