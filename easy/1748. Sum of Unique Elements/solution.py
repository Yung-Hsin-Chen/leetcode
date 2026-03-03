from collections import Counter

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        counts = Counter(nums)

        ans = 0
        for num, count in counts.items():
            if count == 1:
                ans += num

        return ans
    