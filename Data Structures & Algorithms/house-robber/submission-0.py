class Solution:
    def rob(self, nums: List[int]) -> int:
        left = 0
        right = 0

        for idx in range(len(nums)):
            if idx % 2 == 0:
                right += nums[idx]
            else:
                left += nums[idx]
        return max(left, right)
        