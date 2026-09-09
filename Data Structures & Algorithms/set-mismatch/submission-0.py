class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []

        for idx in range(1, len(nums) + 1):
            if idx != nums[idx-1]:
                return [nums[idx-1], idx]
        