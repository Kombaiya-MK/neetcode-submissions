class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # print("looped")
            mid = left + (right - left) // 2
            # print(mid)
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target >= nums[mid]:
                    left = mid
                else:
                    right = mid
        return -1 

        