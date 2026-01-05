# Problem

Given a string `s` consisting of lowercase English letters, return the first letter to appear twice.

Note:

- A letter `a` appears twice before another letter `b` if the second occurrence of `a` is before the second occurrence of `b`.
- `s` will contain at least one letter that appears twice.
 

Example 1:

> **Input:** s = "abccbaacz"\
> **Output:** "c"\
> **Explanation:**\
> The letter 'a' appears on the indexes 0, 5 and 6.\
> The letter 'b' appears on the indexes 1 and 4.\
> The letter 'c' appears on the indexes 2, 3 and 7.\
> The letter 'z' appears on the index 8.\
> The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

Example 2:

> **Input:** s = "abcdd"\
> **Output:** "d"\
> **Explanation:** The only letter that appears twice is 'd' so we return 'd'.
 

Constraints:

- `2 <= s.length <= 100`
- `s` consists of lowercase English letters.
- `s` has at least one repeated letter.

# Solution

The goal is to find the first letter that appears twice in the string, where “first” is determined by which letter’s second occurrence appears earliest in the string.

A naive approach would be to count all character frequencies and then compare the positions of their second occurrences. However, this is unnecessary and more complex than needed.

This solution uses a set to keep track of letters that have already been seen while scanning the string from left to right.

Instead of analysing the entire string first, we process it one character at a time. For each character `c`, we check whether it has appeared before.

If `c` is already in the seen set, this means we have just encountered its second occurrence, and because we are scanning from left to right, this must be the earliest second occurrence among all letters. We can therefore return `c` immediately.

If `c` has not been seen before, we add it to the set and continue.

This works because the first character whose second appearance is encountered during the scan is exactly the character the problem asks for.

Complexity:
- **Time Complexity:** `O(n)` because we iterate through the string once.
- **Space Complexity:** `O(1)` because the set can contain at most 26 lowercase English letters.