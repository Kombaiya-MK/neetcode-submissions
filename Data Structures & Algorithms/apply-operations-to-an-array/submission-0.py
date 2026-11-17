class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        
        while j < len(nums):
            
            if nums[i] == nums[j]:
                nums[i] += nums[i]
                nums[j] = 0
            i += 1
            j += 1
        
        k = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[k], nums[idx] = nums[idx], nums[k]
                k += 1
        return nums