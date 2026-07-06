import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlength = sys.maxsize
        windowSum = 0
        idx = 0
        left = 0
        while idx < len(nums):
            windowSum += nums[idx]
            print(windowSum)
            
            while windowSum >= target:
                minlength = min(minlength, idx - left + 1)
                windowSum -= nums[left]
                left += 1

            idx += 1
            
        return 0 if minlength == sys.maxsize else minlength
            

