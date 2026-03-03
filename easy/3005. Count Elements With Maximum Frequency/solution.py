from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counts = Counter(nums)

        freqs = counts.values()
        max_freq = max(freqs)

        ans = 0
        for f in freqs:
            if f==max_freq:
                ans += f
        return ans
    