class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        for idx in range(1, len(self.nums)):
            self.nums[idx] = self.nums[idx] + self.nums[idx - 1]
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.nums[right] - self.nums[left - 1]
        return self.nums[right]