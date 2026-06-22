class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hashMap:
                return [hashMap[remainder], i]
            else:
                hashMap[nums[i]] = i
        