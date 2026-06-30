class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        idx = 0
        n = len(nums)
        while idx < n:
            currentIdx = nums[idx] - 1

            if 1 <= nums[idx] <= n and nums[idx] != nums[currentIdx]:
                nums[idx], nums[currentIdx] = nums[currentIdx], nums[idx]

            else:
                idx += 1
        print(nums)
        
        for idx in range(n):
            if nums[idx] != idx + 1:
                return idx + 1
        return n

        # print(nums)