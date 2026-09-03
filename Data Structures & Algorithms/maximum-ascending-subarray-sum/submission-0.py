class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        currSum = 0
        curVal = 0

        for idx in range(len(nums)):
            if nums[idx] <= curVal:
                currSum = 0
            currSum += nums[idx]
            curVal = nums[idx]
            maxSum = max(maxSum, currSum)
        return maxSum
        