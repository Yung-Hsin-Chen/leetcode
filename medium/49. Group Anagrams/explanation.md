# Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.


Example 1:

> **Input:** strs = ["eat","tea","tan","ate","nat","bat"]\
> **Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]\
> **Explanation:** There is no string in `strs` that can be rearranged to form "bat". The strings "nat" and "tan" are anagrams as they can be rearranged to form each other. The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

> Input: strs = [""]\
> Output: [[""]]

Example 3:

> Input: strs = ["a"]\
> Output: [["a"]]

 

Constraints:

- `1 <= strs.length <= 104`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

# Solution

The goal is to group together strings that are anagrams, meaning they contain exactly the same characters but possibly in a different order.

A direct comparison of every pair of strings would be inefficient, especially when the list is large. Instead, this solution uses a key observation:

Two strings are anagrams if their sorted characters are identical.

For example:
- "eat", "tea", and "ate" all become "aet" after sorting.
- "tan" and "nat" both become "ant".

The solution uses a `defaultdict(list)` to group strings by this sorted representation.

We iterate through each string in `strs`. For each string:
- Sort its characters.
- Join them back into a string to create a canonical key.
- Append the original string to the list corresponding to that key.

All anagrams will share the same sorted key and therefore end up in the same group.

Finally, we return all grouped lists using `list(ans.values())`.

### Complexity:
- **Time Complexity:** O(n * k log k) where n is the number of strings and k is the maximum length of a string (due to sorting each string).
- **Space Complexity:** O(n * k) for storing the grouped strings.