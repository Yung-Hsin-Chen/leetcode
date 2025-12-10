class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        if len(nums) == 1:
            self._prefix = nums
        else:
            self._prefix = [nums[0]]
            for i in range(1, len(nums)):
                self._prefix.append(self._prefix[i-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix[right] - self._prefix[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)