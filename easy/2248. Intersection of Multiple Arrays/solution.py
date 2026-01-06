from collections import defaultdict

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        counts = defaultdict(int)
        for array in nums:
            for num in array:
                counts[num] += 1
        
        ans = []
        for num, count in counts.items():
            if count==len(nums):
                ans.append(num)

        return sorted(ans)
    