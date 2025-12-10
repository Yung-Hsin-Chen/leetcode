class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while (i<len(nums)) and (j<len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                j += 1
                i += 1
            else:
                j += 1
        
        while i < len(nums):
            nums[i] = 0
            i += 1
        
        return nums