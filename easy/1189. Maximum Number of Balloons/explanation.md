Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

> Input: text = "nlaebolko"\
> Output: 1

Example 2:

> Input: text = "loonbalxballpoon"\
> Output: 2

Example 3:

> Input: text = "leetcode"\
> Output: 0

Constraints:

- `1 <= text.length <= 104`
- text consists of lower case English letters only.

# Solution

The goal is to determine how many times the word “balloon” can be formed using the characters from the given string, where each character can be used at most once.

The key idea is to count how many times each required character appears in the string. We use `Counter` to create a frequency map of all characters in text.

The word "balloon" requires:
	•	'b' once
	•	'a' once
	•	'n' once
	•	'l' twice
	•	'o' twice

This means the limiting factor is the character with the smallest available count relative to its requirement. For 'l' and 'o', we divide their counts by 2 because each instance of "balloon" needs two of them.

By taking the minimum among these adjusted counts, we ensure that all required letters are available for each instance of the word.

The result of this minimum calculation is the maximum number of times "balloon" can be formed from the given string.

Complexity:
- **Time Complexity:** `O(n)` because we count characters in the string once.
- **Space Complexity:** `O(1)` because we only store counts for a fixed set of lowercase English letters.