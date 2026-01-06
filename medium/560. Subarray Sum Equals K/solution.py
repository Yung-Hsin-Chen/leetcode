from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        if len(nums)==1:
            return 1 if nums[0]==k else 0
        
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        curr_sum = 0
        ans = 0
        for num in nums:
            curr_sum += num
            ans += prefix_count[curr_sum - k]
            prefix_count[curr_sum] += 1

        return ans
