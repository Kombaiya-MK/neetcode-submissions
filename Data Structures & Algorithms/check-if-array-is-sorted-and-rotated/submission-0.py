class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for idx in range(n):
            if nums[idx] > nums[(idx + 1) % n]:
                count += 1
        
        return count <= 1
        