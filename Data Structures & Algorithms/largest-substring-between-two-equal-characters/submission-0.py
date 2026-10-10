class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        freq = {}
        maxlength = -1
        for idx in range(len(s)):

            if s[idx] in freq:
                maxlength = max(maxlength, idx - freq[s[idx]] - 1)
            else:
                freq[s[idx]] = idx
        return maxlength

        