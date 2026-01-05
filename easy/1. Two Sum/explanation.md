# Problem

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

> **Input:** nums = [2,7,11,15], target = 9\
> **Output:** [0,1]\
> **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

> **Input:** nums = [3,2,4], target = 6\
> **Output:** [1,2]

Example 3:

> **Input:** nums = [3,3], target = 6\
> **Output:** [0,1]
 

Constraints:

- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than `O(n^2)` time complexity?

# Solution

The goal is to find two different indices in the array such that the numbers at those indices add up to target. A brute-force approach would check every possible pair, but that takes `O(n²)` time and is inefficient for large inputs.

This solution uses a hash map (dictionary) to reduce the time complexity to `O(n)`.

Instead of checking all pairs, we process the array once, keeping track of numbers we have already seen and their indices.

For each number `nums[i]`, we ask:

> “What number would I need to have seen before so that together with `nums[i]` they sum to target?”

That number is called the complement:

```
complement = target - nums[i]
```
If the complement already exists in the hash map, we have found the solution and return the stored index and the current index.

If not, we store the current number and its index in the map for future checks.

This works because we only match the current element with previously seen elements, so the same element is never used twice.

Complexity:
- **Time Complexity:** O(n) because we iterate through the array once and each hash map lookup is constant time on average.
- **Space Complexity:** O(n) because the hash map may store up to `n` elements.

