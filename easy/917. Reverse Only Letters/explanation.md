# Problem

Given a string `s`, reverse the string according to the following rules:

- All the characters that are not English letters remain in the same position.
- All the English letters (lowercase or uppercase) should be reversed.
- Return `s` after reversing it.

 

Example 1:

> **Input:** s = "ab-cd"\
> **Output:** "dc-ba"

Example 2:

> **Input:** s = "a-bC-dEf-ghIj"\
> **Output:** "j-Ih-gfE-dCba"

Example 3:

> **Input:** s = "Test1ng-Leet=code-Q!"\
> **Output:** "Qedo1ct-eeLg=ntse-T!"
 

Constraints:

- `1 <= s.length <= 100`
- `s` consists of characters with ASCII values in the range `[33, 122]`.
- `s` does not contain `'\"'` or `'\\'`.

# Solution

The goal is to reverse only the letters in the string while keeping every non-letter character exactly where it already is. This is a perfect setting for the two-pointer technique, because the characters that matter (letters) are scattered among characters that must remain fixed in place.

Imagine placing one pointer at the start of the string and another at the end. The idea is to walk these pointers inward, searching for letters. When both pointers land on letters, those two letters are swapped. When a pointer lands on something that is not a letter, it simply moves past it, because that character must stay exactly where it is. In other words, the non-letter characters act like stones embedded in the string: they cannot move, so the pointers must walk around them.

This leads to a simple rhythm.
The left pointer walks forward until it reaches a letter.
The right pointer walks backward until it reaches a letter.
If both pointers are now pointing at letters, the letters are swapped.
After the swap, both pointers move one step inward, and the search continues.

An important detail is that each inner search—where a pointer skips past non-letters—must stop if the two pointers cross. Otherwise the pointer might walk past the end of the valid region. By checking that the left pointer is still left of the right pointer before advancing, the algorithm avoids stepping outside the string even in cases where the string contains no letters at all.

Because each pointer only moves forward through the string once, each character is inspected at most a couple of times. Non-letters are quickly skipped, and letters are swapped once at most. This gives the algorithm linear time complexity in relation to the length of the string. The only additional space used is a simple list form of the string, which allows in-place swapping.

The result is produced when the two pointers meet or cross. At that moment, all the letters have been reversed in order, and all non-letters have stayed exactly where they originally were. Converting the list of characters back into a string yields the final output.

- **Time complexity:** O(n)
- **Space complexity:** O(n)