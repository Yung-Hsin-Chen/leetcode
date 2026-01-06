from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = Counter(s)
        return True if len(set(counts.values()))==1 else False
    