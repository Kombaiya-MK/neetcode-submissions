class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        minLength = min(len(word1), len(word2))

        left = 0
        ans = ''
        while left < minLength:
            ans += word1[left] + word2[left]
            left += 1
        
        if left < len(word1):
            ans += word1[left:]
        
        elif left < len(word2):
            ans += word2[left:]
        
        return ans


        