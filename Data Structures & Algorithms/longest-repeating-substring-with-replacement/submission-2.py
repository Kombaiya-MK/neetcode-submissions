class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlength = 0
        freqMap = {}
        left = 0
        maxFreq = 0
        for idx in range(len(s)):
            freqMap[s[idx]] = freqMap.get(s[idx], 0) + 1
            maxFreq = max(maxFreq, freqMap[s[idx]])

            while (idx - left + 1) - maxFreq > k:
                freqMap[s[idx]] -= 1
                left += 1
            
            maxlength = max(maxlength, idx - left + 1)
        return maxlength
        