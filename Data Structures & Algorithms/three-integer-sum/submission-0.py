class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for idx in range(len(nums)):


            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                currentSum = nums[idx] + nums[left] + nums[right]
                if currentSum == 0:
                    ans.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif currentSum > 0:
                    right -= 1
                else:
                    left += 1
        return ans

