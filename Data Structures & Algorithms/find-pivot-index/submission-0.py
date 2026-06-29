class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        rightSum = 0

        for i in range(len(nums)):
            if rightSum == totalSum - nums[i]:
                return i
            rightSum += nums[i]
            totalSum -= nums[i]
        return -1
        
                