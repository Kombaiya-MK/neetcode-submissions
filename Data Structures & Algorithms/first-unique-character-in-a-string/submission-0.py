class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for idx in range(len(s)):
            if s[idx] in freq:
                freq[s[idx]] = -1
            else:
                freq[s[idx]] = idx
        
        for key in freq:
            if freq[key] != -1:
                return freq[key]
        return -1
        