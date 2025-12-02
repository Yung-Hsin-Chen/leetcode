# Problem

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

 

Example 1:

> **Input:** s = ["h","e","l","l","o"]\
> **Output:** ["o","l","l","e","h"]

Example 2:

> **Input:** s = ["H","a","n","n","a","h"]\
> **Output:** ["h","a","n","n","a","H"]
 

Constraints:

- `1 <= s.length <= 105`
- `s[i]` is a printable ascii character.

# Solution

The solution uses two pointers, `l` and `r`. As the two pointers move inward toward the center of the array, they swap the elements in each step. The time complexity of this method is `O(n)`, and the space complexity is `O(1)`.