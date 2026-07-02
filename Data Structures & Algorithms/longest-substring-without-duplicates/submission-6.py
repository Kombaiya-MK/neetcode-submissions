class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        hashMap = {}
        n = len(s)
        k = 0
        for idx in range(n):
            if s[idx] in hashMap:
                k = hashMap[s[idx]] + 1
            
            hashMap[s[idx]] = idx
            maxlength = max(maxlength, idx - k + 1)
        return maxlength

        