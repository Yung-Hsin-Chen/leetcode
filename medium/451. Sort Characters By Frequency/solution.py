from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        counts_tuple = []

        for char, count in counts.items():
            counts_tuple.append((char, count))

        counts_tuple = sorted(counts_tuple, key=lambda x: x[1], reverse=True)

        ans = ""
        for item in counts_tuple:
            char, count = item
            ans += char*count

        return ans
    