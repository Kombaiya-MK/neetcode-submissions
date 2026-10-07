class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = False
        isDecreasing = False

        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx-1]:
                isIncreasing = True
            
            if nums[idx] < nums[idx-1]:
                isDecreasing = True
        
        return not (isIncreasing and isDecreasing)
        