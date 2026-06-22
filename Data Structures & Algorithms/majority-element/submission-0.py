class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        
        maxElement = nums[0]
        maxCount = hashMap[nums[0]]

        for i in hashMap:
            print(i)
            print(hashMap[i])
            if hashMap[i] > maxCount:
                maxCount = hashMap[i]
                maxElement = i
        return maxElement
        