from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        counts = Counter(nums)
        
        ans = -1
        for num, count in counts.items():
            if count==1:
                ans = max(ans, num)
        
        return ans