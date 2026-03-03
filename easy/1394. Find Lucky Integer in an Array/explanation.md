# Problem

Given an array of integers `arr`, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return `-1`.

 

Example 1:

> **Input:** arr = [2,2,3,4]\
> **Output:** 2\
> **Explanation:** The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:

> **Input:** arr = [1,2,2,3,3,3]\
> **Output:** 3\
> **Explanation:** 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:

> **Input:** arr = [2,2,2,3,3]\
> **Output:** -1\
> **Explanation:** There are no lucky numbers in the array.
 

Constraints:

- `1 <= arr.length <= 500`
- `1 <= arr[i] <= 500`

# Solution

The goal is to find the largest lucky integer in the array. A lucky integer is defined as a number whose frequency is equal to its value.

To solve this efficiently, we first count how many times each number appears in the array. We use `Counter` to build a frequency map where:
- The key is the number.
- The value is how many times it appears.

Next, we iterate through each `(number, count)` pair in the frequency map. For each number, we check whether it satisfies the lucky condition:
```python
number == count
```
If it does, we compare it with the current `max_lucky` value and keep the larger one. This ensures that if multiple lucky numbers exist, we return the largest one.

If no number satisfies the condition, `max_lucky` remains `-1`, which is returned as required.

### Complexity:
- **Time Complexity:** O(n) because we traverse the array once to build the frequency map and once to check the lucky condition.
- **Space Complexity:** O(n) in the worst case if all elements are distinct.