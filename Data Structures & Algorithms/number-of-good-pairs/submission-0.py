from collections import defaultdict 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = defaultdict(list)
        pairs = 0

        for idx in range(len(nums)):
            if nums[idx] in hashMap:
                pairs += len(hashMap[nums[idx]])
                hashMap[nums[idx]].append(idx)
            else:
                hashMap[nums[idx]].append(idx)
        # print(hashMap)
        return pairs

        