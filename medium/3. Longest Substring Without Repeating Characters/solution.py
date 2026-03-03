from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        ans = 0
        curr = 0
        l = -1

        for char in s:
            curr += 1
            while counts[char] > 0:
                l += 1
                curr -= 1
                counts[s[l]] -= 1
            counts[char] += 1
            ans = max(ans, curr)

        return ans
