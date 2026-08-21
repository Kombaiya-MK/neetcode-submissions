class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        n = len(nums)
        if n < 2:
            return True
        for idx in range(1, n):
            if k >= n - 1:
                return True
            k += nums[k]
        return False

        