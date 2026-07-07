class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        maxlength = 0
        for idx in range(len(s)):
            if s[idx] in hashMap:
                if hashMap[s[idx]] - idx <= k:
                    maxlength = max(maxlength, idx - hashMap[s[idx]] + 1)
                    k -= hashMap[s[idx]] - idx
                else:
                    hashMap[s[idx]] = idx
            else:
                hashMap[s[idx]] = idx
        return maxlength
        