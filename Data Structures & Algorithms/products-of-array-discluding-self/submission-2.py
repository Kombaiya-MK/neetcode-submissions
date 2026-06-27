class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            prefix = 1
            suffix = 1
            left, right = 0, len(nums) - 1
            while left < i or right > i:
                if left < i:
                    prefix *= nums[left]
                    left += 1
                elif right > i:
                    suffix *= nums[right]
                    right -= 1
            # print(prefix, suffix)
            ans.append(prefix*suffix)

        return ans

        