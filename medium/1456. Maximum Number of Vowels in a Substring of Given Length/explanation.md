# Problem

Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

> **Input:** s = "abciiidef", k = 3\
> **Output:** 3\
> **Explanation:** The substring "iii" contains 3 vowel letters.

Example 2:

> **Input:** s = "aeiou", k = 2\
> **Output:** 2\
> **Explanation:** Any substring of length 2 contains 2 vowels.

Example 3:

> **Input:** s = "leetcode", k = 3\
> **Output:** 2\
> **Explanation:** "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

- `1 <= s.length <= 105`
- `s` consists of lowercase English letters.
- `1 <= k <= s.length`

# Solution

The problem asks for the maximum number of vowels contained in any substring of fixed length. Because every substring we compare has the same size, the most natural tool is a sliding window that keeps its width constant while we move across the string.

To begin, imagine placing a window over the first k characters of the string. Count how many vowels exist inside this initial window. This gives you a starting point: the best result so far is simply the number of vowels in this first block.

Once the initial window has been evaluated, the sliding process starts. Move the window one step to the right. When you do this, two things change. A new character enters from the right, and an old character leaves from the left. If the incoming character is a vowel, the count increases by one. If the outgoing character is a vowel, the count decreases by one. This keeps the count accurate without ever recounting the entire window.

After updating the count, compare it against the best value seen so far and update the maximum when necessary. Then move the window again. This simple rhythm repeats: add the effect of the new character, remove the effect of the old one, update the maximum, and continue until the window has moved across the entire string.

- **Time complexity:** O(n)
- **Space complexity:** O(1)