# Problem

Given a string `s`, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

> **Input:** s = "tree"\
> **Output:** "eert"\
> **Explanation:** 'e' appears twice while 'r' and 't' both appear once. So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

> **Input:** s = "cccaaa"\
> **Output:** "aaaccc"\
> **Explanation:** Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers. Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

> **Input:** s = "Aabb"
> **Output:** "bbAa"
> **Explanation:** "bbaA" is also a valid answer, but "Aabb" is incorrect. Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

- `1 <= s.length <= 5 * 105`
- `s` consists of uppercase and lowercase English letters and digits.

# Solution

The goal is to rearrange the characters of the string so that they appear in decreasing order of frequency. Characters with higher frequency must appear before those with lower frequency. If multiple characters have the same frequency, any order among them is acceptable.

First, we use `Counter` to count how many times each character appears in the string. This gives us a mapping from each character to its frequency.

Next, we convert the frequency map into a list of `(character, count)` tuples. We then sort this list in descending order based on the frequency using:
```python
key=lambda x: x[1]
```
with `reverse=True`.

After sorting, characters with the highest frequency come first.

Finally, we build the result string by repeating each character according to its frequency `(char * count)` and appending it to the result. This ensures that identical characters stay grouped together, as required by the problem.

If multiple characters share the same frequency, their relative order does not matter, since the problem allows any valid arrangement.

### Complexity:
- Time Complexity: O(n + k log k) where n is the length of the string and k is the number of distinct characters (at most the character set size). But since the string consists of only uppercase letters (26), lowercase letters (26) and digits (10). That’s at most 62 distinct characters. So under this constraint, O(n + k log k) → O(n + 1) → O(n).
- Space Complexity: O(n) for storing the result and frequency structures.

