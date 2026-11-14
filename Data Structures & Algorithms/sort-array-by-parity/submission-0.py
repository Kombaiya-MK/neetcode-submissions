class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k = 0
        for idx in range(len(nums)):
            if nums[idx] % 2 == 0:
                nums[k], nums[idx] = nums[idx], nums[k]
                k += 1
        return nums
        