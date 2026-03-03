# Problem

You are given an array `nums` consisting of positive integers.

Return the total frequencies of elements in `nums` such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

> Input: nums = [1,2,2,3,1,4]\
> Output: 4\
> Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array. So the number of elements in the array with maximum frequency is 4.

Example 2:

> Input: nums = [1,2,3,4,5]\
> Output: 5\
> Explanation: All elements of the array have a frequency of 1 which is the maximum. So the number of elements in the array with maximum frequency is 5.
 

Constraints:

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

# Solution

The goal is to compute the total number of elements whose frequency is equal to the maximum frequency in the array.

First, we use `Counter` to count how many times each number appears in `nums`. This gives us a mapping from each element to its frequency.

Next, we determine the maximum frequency by taking the maximum value from `counts.values()`. This represents the highest number of occurrences of any element in the array.

Finally, we iterate through all frequencies again. For every element whose frequency equals `max_freq`, we add that frequency to the result. Since each such element appears `max_freq` times, we accumulate the total number of elements that belong to the most frequent group.

For example:
- If two numbers each appear twice, and `2` is the maximum frequency, then we add `2 + 2 = 4`.
- If all numbers appear once, then the maximum frequency is `1`, and we sum all ones, resulting in the array length.

Complexity:
- **Time Complexity:** O(n) because we traverse the array once to build the frequency map and once more to compute the result.
- **Space Complexity:** O(n) in the worst case if all elements are distinct.