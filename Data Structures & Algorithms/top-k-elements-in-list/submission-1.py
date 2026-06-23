class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqElements = []
        trackerStack = []

        for i in range(len(nums)):

            if len(trackerStack) > 0 and trackerStack[0] != nums[i]:
                trackerStack.pop()
                trackerStack.append(nums[i])
            
            else:
                trackerStack.append(nums[i])

            if len(trackerStack) == k and nums[i] not in freqElements:
                freqElements.append(nums[i])
                trackerStack = []
        if not freqElements:
            return nums
        return freqElements


        
        