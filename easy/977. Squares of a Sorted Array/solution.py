class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = [0]*len(nums)
        l = 0
        r = len(nums)-1
        curr = len(nums)-1
        
        while l <= r:
            if nums[r]**2 > nums[l]**2:
                ans[curr] = nums[r]**2
                r -= 1
            else:
                ans[curr] = nums[l]**2
                l += 1
            curr -= 1
        return ans
    