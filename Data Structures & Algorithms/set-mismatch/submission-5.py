class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        freq = set()
        n = len(nums)
        for num in nums:
            if num in freq:
                ans.append(num)
            else:
                freq.add(num)
        val = ((n * (n + 1)) // 2) - sum(freq)
        ans.append(val)
        return ans