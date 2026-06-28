class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap  = {}

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
            
        ans = []
        n = len(nums)
        for num in hashMap:
            if hashMap[num] > (n//3):
                ans.append(num)
        return ans     