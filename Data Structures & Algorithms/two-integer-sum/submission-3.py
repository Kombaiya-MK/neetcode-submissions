class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
    ## two pointers

        left, right = 0, len(nums) - 1

        while left < right:
            val = nums[left] + nums[right]

            if val == target:
                return [left, right]
            
            elif val < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
        