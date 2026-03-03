# Problem

Given a string `s`, find the length of the longest substring without duplicate characters.

 

Example 1:

> Input: s = "abcabcbb"\
> Output: 3\
> Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

> Input: s = "bbbbb"\
> Output: 1\
> Explanation: The answer is "b", with the length of 1.

Example 3:

> Input: s = "pwwkew"\
> Output: 3\
> Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols and spaces.

# Solution

The goal is to find the length of the longest contiguous substring that contains no repeated characters.

A brute-force approach would try every substring and check whether it contains duplicates, but that would take `O(n²)` time (or worse) for long strings. This solution uses the sliding window technique to achieve linear time.

We maintain a window of characters that always contains unique characters only. The window is represented by two pointers:
- `l` is the index just before the start of the current window (initialise it as `-1`).
- The loop iterates through the string from left to right, effectively extending the right end of the window one character at a time.

We also keep a dictionary counts that stores how many times each character appears in the current window.

For each new character char we add to the window:
- We increase `curr` (the current window length).
- If `char` is already in the window (`counts[char] > 0`), the window is no longer valid.
  
To fix this, we shrink the window from the left: we move `l` forward and remove characters from the window (decrement their counts and reduce curr) until char is no longer duplicated.
	•	Once the window contains unique characters again, we add `char` to the window by incrementing `counts[char]`.
	•	We update ans with the maximum window length seen so far.

Because each character is added to the window once and removed at most once, the two pointers only move forward and never move backward, which keeps the algorithm efficient.

### Complexity:
- **Time Complexity:** O(n) because each character is processed at most twice (once when added, once when removed).
- **Space Complexity:** O(k) where k is the number of distinct characters in the window (bounded by the character set size).