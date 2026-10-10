class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        palindromeLength = 0
        hasOdd = False
        for ch in freq:
            if freq[ch] & 1:
                palindromeLength += freq[ch] - 1
                hasOdd = True
            else:
                palindromeLength += freq[ch]
        if hasOdd:
            palindromeLength += 1
        return palindromeLength