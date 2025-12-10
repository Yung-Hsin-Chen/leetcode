class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])

        for i in range(len(nums)):
            left = prefix[i] - nums[i]
            right = prefix[-1] - prefix[i]
            if left == right:
                return i
            
        return -1
    