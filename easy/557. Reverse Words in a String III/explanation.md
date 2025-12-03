# Problem

Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

> **Input:** s = "Let's take LeetCode contest"\
> **Output:** "s'teL ekat edoCteeL tsetnoc"

Example 2:

> **Input:** s = "Mr Ding"\
> **Output:** "rM gniD"
 

Constraints:

- `1 <= s.length <= 5 * 104`
- `s` contains printable ASCII characters.
- `s` does not contain any leading or trailing spaces.
- There is at least one word in `s`.
- All the words in `s` are separated by a single space.

# Explanation

The solution works by splitting the input string into its individual words, reversing each word separately, and then joining the reversed words back together with spaces. Since the whitespace and the original order of the words must be preserved, only the characters inside each word are reversed.

The code begins by using `s.split(" ")` to break the string into a list of words. Each word is then converted into a list of characters so it can be reversed in place. Two pointers, `l` and `r`, start at the left and right ends of the word. The characters at these positions are swapped, and the pointers move inward until they meet. This reverses the characters of the word without using extra data structures. After reversing, the characters are joined back into a string and appended to the result list. Once all words are processed, the reversed words are joined using `" ".join(ans)` to reconstruct the final sentence with spaces preserved.

- **Time complexity:** `O(n)` — each character is processed once.

- **Space complexity:** O(n) - storing split words + output.