class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + (high - low)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid - 1
            print([low, high, mid])
            
        return mid if mid == 0 else mid + 1
        