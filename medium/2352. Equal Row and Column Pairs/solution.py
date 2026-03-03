from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        counts = defaultdict(int)
        cols = []
        ans = 0

        for row in grid:
            counts[tuple(row)] += 1

        for i in range(len(row)):
            col = []
            for row in grid:
                col.append(row[i])
            cols.append(col)

        for col in cols:
            ans += counts[tuple(col)]

        return ans
    