from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        index = defaultdict(lambda: None)
        ans = float("inf")

        for i, c in enumerate(cards):
            if index[c] != None:
                ans = min(ans, i-index[c]+1)
            index[c] = i

        return ans if ans != float("inf") else -1
    