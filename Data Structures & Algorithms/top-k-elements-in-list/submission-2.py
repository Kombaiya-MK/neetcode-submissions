class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1


        result = sorted(
        hashMap.keys(),
        key=lambda x: hashMap[x],
        reverse=True)

        return result[:k]
        
            
        


        
        