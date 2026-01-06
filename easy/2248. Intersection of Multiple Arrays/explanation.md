# Problem

Given a 2D integer array `nums` where `nums[i]` is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

Example 1:

> Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]\
> Output: [3,4]\
> Explanation: The only integers present in each of `nums[0] = [3,1,2,4,5]`, `nums[1] = [1,2,3,4]`, and `nums[2] = [3,4,5,6]` are 3 and 4, so we return `[3,4]`.

Example 2:

> Input: nums = [[1,2,3],[4,5,6]]\
> Output: []\
> Explanation: There does not exist any integer present both in `nums[0]` and `nums[1]`, so we return an empty list `[]`.
 

Constraints:

- `1 <= nums.length <= 1000`
- `1 <= sum(nums[i].length) <= 1000`
- `1 <= nums[i][j] <= 1000`
- All the values of `nums[i]` are unique.

# Solution

The goal is to find all integers that appear in every subarray of `nums` and return them sorted in ascending order.

A brute-force approach would compare each number across all arrays individually, but this would be inefficient and harder to manage. Instead, this solution uses a frequency-counting strategy.

We use a dictionary (`defaultdict`) to count how many different arrays each number appears in. Since every subarray contains distinct values, we can safely increment the count for every number we encounter without worrying about duplicates within the same subarray.

We iterate through each array in `nums, and for each number, increment its count in the dictionary. After processing all arrays, the dictionary tells us how many arrays each number appeared in.

If a number’s count is exactly equal to the number of subarrays (`len(nums)`), then that number appeared in every array and should be included in the result.

Finally, we sort the collected numbers in ascending order before returning them, as required by the problem.

Complexity:
- **Time Complexity:** `O(n)` where `n` is the total number of elements across all subarrays.
- **Space Complexity:** `O(n)` for storing the counts of each distinct number.