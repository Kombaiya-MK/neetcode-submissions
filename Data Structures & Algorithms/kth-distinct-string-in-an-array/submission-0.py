class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        freq = {}

        for st in arr:
            if st not in freq:
                freq[st] = 1
            else:
                del freq[st]
        
        for key in freq:
            k -= 1
            if k == 0:
                return key
        return ""
