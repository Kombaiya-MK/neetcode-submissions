class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        palindromeLength = 0
        maxOddChar = 0
        for ch in freq:
            if freq[ch] & 1:
                maxOddChar = max(maxOddChar, freq[ch])
            else:
                palindromeLength += freq[ch]
        return palindromeLength + maxOddChar