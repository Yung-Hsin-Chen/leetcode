class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        flipped = 0
        max_subarray = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                flipped += 1
            while flipped > k:
                if nums[l] == 0:
                    flipped -= 1
                l += 1
            max_subarray = max(max_subarray, r-l+1)
        return max_subarray
    