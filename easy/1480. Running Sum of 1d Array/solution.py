class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        if len(nums)==1:
            return nums

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1]+nums[i])

        return prefix
    