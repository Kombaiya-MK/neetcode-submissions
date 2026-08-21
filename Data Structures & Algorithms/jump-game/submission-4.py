class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        n = len(nums)
        if n < 2:
            return True
        for idx in range(1, n):
            k += nums[k]
            if k >= n - 1:
                return True
        return False

        