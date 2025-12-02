class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total_sum = 0
        for i in nums:
            total_sum += i

        left_sum, right_sum = 0, total_sum
        valid_split = 0
        for i in range(len(nums)-1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if right_sum <= left_sum:
                valid_split += 1
        return valid_split
    