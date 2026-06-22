from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            hashMap = defaultdict(list)

            for i in strs:
                sortedValue = tuple(sorted(i))
                hashMap[sortedValue].append(i)
            # print(dict(hashMap))

            return list((hashMap).values())
        
        

        
        