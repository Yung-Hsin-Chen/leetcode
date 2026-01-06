from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        curr_odd = 0
        counts = defaultdict(int)
        counts[0] = 1
        ans = 0
        for num in nums:
            curr_odd += num % 2
            ans += counts[curr_odd - k]
            counts[curr_odd] += 1
        
        return ans
    