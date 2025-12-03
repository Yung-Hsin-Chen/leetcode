class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        # startValue + min_prefix >= 1
        # startValue >= 1 - min_prefix
        curr_sum = 0
        min_sum = inf
        for v in nums:
            curr_sum += v
            min_sum = min(curr_sum, min_sum)
        return max(1 - min_sum, 1)
    