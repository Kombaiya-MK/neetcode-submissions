class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        freq = {}
        nums.sort()
        for num in nums:
            if num in freq:
                ans.append(num)
                break
            else:
                freq[num] = 1
        for idx in range(1, len(nums) + 1):
            if idx != nums[idx-1]:
                ans.append(idx)
                return ans
        return ans
        