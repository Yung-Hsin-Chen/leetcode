# Problem

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the `stones` you have are also `jewels`.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

 

Example 1:

> Input: jewels = "aA", stones = "aAAbbbb"\
> Output: 3

Example 2:

> Input: jewels = "z", stones = "ZZ"\
> Output: 0
 

Constraints:

- `1 <= jewels.length, stones.length <= 50`
- `jewels` and `stones` consist of only English letters.
- All the characters of `jewels` are unique.

# Solution

The goal is to count how many characters in `stones` also appear in `jewels`, taking into account that letters are case sensitive.

A brute-force approach would check, for each character in `stones`, whether it exists in `jewels` by scanning the `jewels` string each time. This would result in `O(n * m)` time complexity, where `n` is the length of `stones` and `m` is the length of `jewels`.

To improve efficiency, this solution converts `jewels` into a set. A set allows constant-time membership checks on average, which makes the lookup much faster.

We first create `jewel_set = set(jewels)`, so we can quickly determine whether a character is a jewel. Then, we iterate through each character in `stones`. If the character exists in `jewel_set`, we increment a counter.

Since each stone is checked exactly once and set lookups are constant time, this approach is efficient and straightforward.

Finally, we return the total count of stones that are jewels.

Complexity:
- **Time Complexity:** O(n + m) where n is the length of stones and m is the length of jewels.
  - set(jewels) → this loops over jewels once. Cost: O(m)
  - Loop over stones. Cost: O(n)
- **Space Complexity:** O(m) for storing the jewels in a set.