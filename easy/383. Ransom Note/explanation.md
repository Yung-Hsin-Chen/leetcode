# Problem

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

 

Example 1:

> Input: ransomNote = "a", magazine = "b"\
> Output: false

Example 2:

> Input: ransomNote = "aa", magazine = "ab"\
> Output: false

Example 3:

> Input: ransomNote = "aa", magazine = "aab"\
> Output: true
 

Constraints:

- `1 <= ransomNote.length, magazine.length <= 105`
- `ransomNote` and `magazine` consist of lowercase English letters.

# Solution

The goal is to determine whether the string `ransomNote` can be formed using the characters from `magazine`, where each `character` in magazine can only be used once.

A straightforward way to approach this is by comparing the frequency of each character in both strings.

First, we count how many times each character appears in `ransomNote`. Then, we count how many times each character appears in `magazine`. This is done using two dictionaries that map characters to their occurrence counts.

After building these frequency maps, we iterate through each character in `ransomNote`. For each character, we check whether `magazine` contains at least as many occurrences as needed. If `magazine` has fewer occurrences of any required character, it is impossible to construct the `ransomNote`, and we return `False`.

If all required characters are available in sufficient quantities, we return `True`.

This approach ensures that every letter is accounted for and that no letter is used more times than it appears in magazine.

Complexity:
- **Time Complexity:** O(n + m) where n is the length of ransomNote and m is the length of magazine, since we traverse both strings once.
- **Space Complexity:** O(1) because there are at most 26 lowercase English letters.