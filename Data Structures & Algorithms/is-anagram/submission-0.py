class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Map = {}
        for i in s:
            if i in Map:
                Map[i] += 1
            else:
                Map[i] = 1
        
        for i in t:
            if i not in Map:
                return False
            else:
                Map[i] -= 1
        
        return len(Map) == 0
            