from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixCount = defaultdict(int)
        prefixCount[0] = 1

        currentSum = 0
        count = 0

        for num in nums:
            currentSum += num
            count += prefixCount[currentSum - goal]
            prefixCount[currentSum] += 1

        return count