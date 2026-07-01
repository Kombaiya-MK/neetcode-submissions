class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        minLength = min(len(word1), len(word2))

        left = 0
        ans = []
        while left < minLength:
            ans.append(word1[left])
            ans.append(word2[left])
            left += 1
        
        while left < len(word1):
            ans.append(word1[left])
            left += 1
        
        while left < len(word2):
            ans.append(word2[left])
            left += 1
        
        return ''.join(ans)


        