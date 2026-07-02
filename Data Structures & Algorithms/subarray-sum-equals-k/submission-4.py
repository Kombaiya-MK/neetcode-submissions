class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        hashMap = {0:1}
        prefixSum = 0

        for idx in range(n):

            prefixSum += nums[idx]

            val = prefixSum - k
            if val in hashMap:
                count += hashMap[val]
            
            if prefixSum in hashMap:
                hashMap[prefixSum] += 1
            else:
                hashMap[prefixSum] = 1
        return count



        