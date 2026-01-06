# Problem

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return `true` if sentence is a pangram, or `false` otherwise.

 

Example 1:

> **Input:** sentence = "thequickbrownfoxjumpsoverthelazydog"\
> **Output:** true\
> **Explanation:** sentence contains at least one of every letter of the English alphabet.

Example 2:

> **Input:** sentence = "leetcode"\
> **Output:** false
 

Constraints:

- `1 <= sentence.length <= 1000`
- sentence consists of lowercase English letters.

# Solution

The goal is to determine whether a given sentence is a pangram, meaning it contains every letter of the English alphabet at least once.

A simple observation helps reduce unnecessary work: since there are 26 letters in the English alphabet, any sentence shorter than 26 characters cannot be a pangram. We can immediately return `False` in that case.

After this early check, the solution uses a set to track unique letters found in the sentence. Sets are ideal here because they automatically handle duplicates.

We iterate through the sentence character by character and add each letter to the set. By the end of the loop, the set will contain all distinct letters that appeared in the sentence.

If the size of the set is exactly 26, it means every lowercase English letter appeared at least once, so the sentence is a pangram. Otherwise, it is not.

This approach is straightforward, efficient, and easy to reason about.

Complexity:
- **Time Complexity:** `O(n)` because we iterate through the sentence once.
- **Space Complexity:** `O(1)` because the set can contain at most 26 lowercase English letters.