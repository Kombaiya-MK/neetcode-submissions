class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, isFirstOccurrence):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = left + (right -left) // 2
                # print(mid, left, right)
                # print(nums[mid])
                if nums[mid] == target:
                    # print("True", mid)
                    ans = mid
                    if isFirstOccurrence:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
    
        return [binarySearch(nums, target, True), binarySearch(nums, target, False)]

        