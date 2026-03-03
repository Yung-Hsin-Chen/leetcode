from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # counts of sum ones and zeros
        counts = defaultdict(lambda: None)
        counts[0] = -1

        prefix = 0
        ans = 0
        for i, num in enumerate(nums):
            prefix += 1 if num==1 else -1
            
            if counts[prefix] != None:
                ans = max(ans, i-counts[prefix])
            else:
                counts[prefix] = i

        return ans
            