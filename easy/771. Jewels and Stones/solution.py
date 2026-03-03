class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        ans = 0

        for s in stones:
            if s in jewel_set:
                ans += 1

        return ans
    