class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ans = 0
        for i in range(k):
            max_ans += nums[i]

        l = 0
        curr = max_ans
        for r in range(k, len(nums)):
            curr += nums[r]
            curr -= nums[l]
            max_ans = max(max_ans, curr)
            r -= 1
            l += 1

        return max_ans/k
    