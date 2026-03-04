from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = Counter(arr)

        if len(set(counts.values()))==len(counts):
            return True

        return False
    