class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if len(nums) < (2*k+1):
            return [(-1)]*len(nums)

        if k == 0:
            return nums

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])

        for i in range(len(nums)):
            if i == k:
                nums[i] = prefix[i+k]//(2*k+1)
            elif (i >= k+1) and (i < len(nums)-k):
                nums[i] = (prefix[i+k] - prefix[i-k-1])//(2*k+1)
            else:
                nums[i] = (-1)
        
        return nums
    