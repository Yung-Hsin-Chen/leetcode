from collections import defaultdict

class Solution:
    def findWinners(self, matches: list[list[int]]) -> List[List[int]]:
        lose_count = defaultdict(int)
        for match in matches:
            win, lose = match[0], match[1]
            lose_count[lose] += 1
            lose_count[win] += 0

        not_lost = sorted([c for c in lose_count if lose_count[c]==0])
        lose_one = sorted([c for c in lose_count if lose_count[c]==1])

        return [not_lost, lose_one]
    