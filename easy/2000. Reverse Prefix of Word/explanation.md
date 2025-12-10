# Problem

Given a 0-indexed string `word` and a character `ch`, reverse the segment of word that starts at index `0` and ends at the index of the first occurrence of `ch` (inclusive). If the character `ch` does not exist in word, do nothing.

For example, if `word = "abcdefd"` and `ch = "d"`, then you should reverse the segment that starts at `0` and ends at `3` (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

 

Example 1:

> **Input:** word = "abcdefd", ch = "d"\
> **Output:** "dcbaefd"\
> **Explanation:** The first occurrence of "d" is at index 3. 
> Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Example 2:

> **Input:** word = "xyxzxe", ch = "z"\
> **Output:** "zxyxxe"\
> **Explanation:** The first and only occurrence of "z" is at index 3.
> Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

Example 3:

> **Input:** word = "abcd", ch = "z"\
> **Output:** "abcd"\
> **Explanation:** "z" does not exist in word.
> You should not do any reverse operation, the resulting string is "abcd".
 

Constraints:

- `1 <= word.length <= 250`
- `word` consists of lowercase English letters.
- `ch` is a lowercase English letter.
  
# Solution
The problem asks us to reverse the beginning of a string only up to the first occurrence of a given character. Everything after that point must remain exactly as it is. This naturally breaks the task into two steps: find the position where the reversal should stop, and then reverse only that segment.

The first step is simply locating the first occurrence of ch. Scanning from the left ensures we identify the earliest position. If the character does not appear at all, then the string should remain unchanged, so we immediately return it.

Once we know the cut-off index, the problem turns into reversing a prefix — the portion from the beginning of the string up to that index. Because Python strings are immutable, we convert the string into a list of characters so we can modify it in place. Then we use two pointers: one starting at the beginning of the prefix and one at the end. These pointers walk inward, swapping characters as they go. Each swap moves a character from its original place to its mirrored position in the reversed prefix.

The reversal stops when the two pointers meet or cross, meaning the segment has been fully reversed. Since only the prefix is touched, and all characters after the first occurrence of ch are left alone, the resulting list of characters now represents the required transformation. Converting the list back into a string produces the final answer.

This method is efficient because both the search for the character and the reversal work in linear time. No unnecessary scanning or copying is done beyond the minimal list conversion required to enable mutation.

- **Time complexity:** O(n) because the algorithm performs two linear operations:
	1.	A scan to find the first occurrence of ch.
	2.	A reversal of at most that many characters.
- **Space complexity:** O(n) because the string is converted into a list of characters.