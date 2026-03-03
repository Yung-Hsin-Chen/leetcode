# Problem

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

 

Example 1:

>Input: nums = [1,2,3,1]\
> Output: true\
> Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:

> Input: nums = [1,2,3,4]\
> Output: false\
> Explanation: All elements are distinct.

Example 3:

> Input: nums = [1,1,1,3,3,4,3,2,4,2]\
> Output: true

 
Constraints:

- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

# Solution

The goal is to determine whether any number appears more than once in the array. If at least one duplicate exists, we return `True`; otherwise, we return `False`.

A brute-force approach would compare every pair of elements, which would take `O(n²)` time. Instead, this solution uses a set to detect duplicates efficiently.

We iterate through the array while maintaining a set called `seen`. For each number:
- If the number is already in `seen`, it means we have encountered it before, so a duplicate exists and we immediately return `True`.
- If it is not in `seen`, we add it to the set and continue.

If the loop completes without finding any duplicates, it means all elements are distinct, and we return `False`.

Using a set allows us to check whether an element has been seen before in constant time on average.

### Complexity:
- **Time Complexity:** O(n) because we traverse the array once and each set lookup is constant time on average.
- **Space Complexity:** O(n) in the worst case if all elements are distinct.