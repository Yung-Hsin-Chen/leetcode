# Problem

Given a string `s`, return `true` if `s` is a good string, or `false` otherwise.

A string `s` is good if all the characters that appear in `s` have the same number of occurrences (i.e., the same frequency).

 

Example 1:

> **Input:** s = "abacbc"\
> **Output:** true\
> **Explanation:** The characters that appear in `s` are `'a'`, `'b'`, and `'c'`. All characters occur 2 times in `s`.

Example 2:

> **Input:** s = "aaabb"\
> **Output:** false\
> **Explanation:** The characters that appear in `s` are `'a'` and `'b'`.
`'a'` occurs 3 times while `'b'` occurs 2 times, which is not the same number of times.
 

Constraints:

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

# Solution

The goal is to determine whether a string is good, meaning that all characters that appear in the string occur the same number of times.

The solution starts by counting how many times each character appears in the string. This is done using `Counter`, which efficiently produces a mapping from characters to their frequencies.

Once we have the frequencies, we only care about the values of this mapping. If all characters occur the same number of times, then all frequency values should be identical.

To check this, we convert the collection of frequency values into a set. If the set has length 1, it means there is only one unique frequency, so all characters occur equally often and the string is good. Otherwise, the string is not good.

Finally, we return the result of this check.

Complexity:
- **Time Complexity:** `O(n)` because we traverse the string once to count character frequencies.
- **Space Complexity:** `O(1)` because there are at most 26 lowercase English letters, so the frequency map has constant size.