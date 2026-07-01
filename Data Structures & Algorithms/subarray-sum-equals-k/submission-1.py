class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        prefix = [nums[0]] * n
        for idx in range(1, n):
            prefix[idx] = prefix[idx - 1] + nums[idx]

        for start in range(n):
            currentSum = 0
            for end in range(start, n):
                if start == 0:
                    currentSum = prefix[end]
                else:
                    currentSum = prefix[end] - prefix[start - 1]
                
                if currentSum == k:
                    count += 1
        return count


        