class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        idx = 0
        n = len(nums)
        while idx < n:

            j = 0
            while nums[idx] != idx + 1 and j < n:
                if nums[j] != j + 1:
                    nums[idx], nums[j] = nums[j], nums[idx]
                j += 1
            idx += 1
        
        for idx in range(n):
            if nums[idx] != idx + 1:
                return idx + 1
        return n

        print(nums)