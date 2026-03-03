from collections import defaultdict

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        digit_sums = defaultdict(int)
        ans = -1

        for num in nums:
            digit_sum = sum([int(x) for x in list(str(num))])
            if digit_sums[digit_sum]:
                ans = max(ans, num+digit_sums[digit_sum])
            digit_sums[digit_sum] = max(digit_sums[digit_sum], num)
        
        return ans
    