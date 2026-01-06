# Problem

You are given an integer array matches where `matches[i] = [winner_i, loser_i]` indicates that the player `winner_i` defeated player `loser_i` in a match.

Return a list answer of size 2 where:

`answer[0]` is a list of all players that have not lost any matches.
`answer[1]` is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:

> **Input:** matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]\
> **Output:** [[1,2,10],[4,5,7,8]]\
> **Explanation:**
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, `answer[0] = [1,2,10]` and `answer[1] = [4,5,7,8]`.

Example 2:

> **Input:** matches = [[2,3],[1,3],[5,4],[6,4]]\
> **Output:** [[1,2,5,6],[]]\
> **Explanation:**
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, `answer[0] = [1,2,5,6]` and `answer[1] = []`.
 

Constraints:

- `1 <= matches.length <= 105`
- `matches[i].length == 2`
- `1 <= winner_i, loser_i <= 105`
- `winner_i != loser_i`
- All `matches[i]` are unique.

# Solution

The goal is to classify players based on how many matches they have lost, considering only players who have played at least one match.

Specifically, we need:
- All players who have not lost any matches
- All players who have lost exactly one match

This solution focuses on counting losses efficiently.

We use a dictionary (lose_count) to record how many times each player has lost. As we iterate through the match list, each match provides a winner and a loser. We increment the loss count for the loser. At the same time, we ensure that winners are also included in the dictionary (with a loss count of zero if they have never lost), so that every player who participated appears in the final result.

After processing all matches, the dictionary contains every player who played at least once, mapped to the number of matches they lost.

We then iterate through this dictionary:
- Players with a loss count of 0 are added to the “not lost” list.
- Players with a loss count of 1 are added to the “lost exactly once” list.

Finally, both lists are sorted in increasing order, as required by the problem, and returned as the final answer.

Complexity:
- **Time Complexity:** `O(n log n)` where `n` is the number of players, due to sorting the result lists.
- **Space Complexity:** `O(n)` for storing loss counts for each player.