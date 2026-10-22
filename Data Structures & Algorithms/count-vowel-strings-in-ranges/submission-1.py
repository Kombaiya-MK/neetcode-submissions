class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = { 'a', 'e', 'i', 'o', 'u'}    
        vowelArray = [0] * (len(words) + 1)
        idx = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels and  word[0] == word[-1]:
                vowelArray[idx + 1] = 1
            idx += 1
        
        ans = []
        
        for idx in range(1, len(vowelArray)):
            vowelArray[idx] = vowelArray[idx - 1] + vowelArray[idx]
        print(vowelArray)

        ans = [0] * len(queries)
        for idx in range(len(queries)):
            ans[idx] = vowelArray[queries[idx][1]+1] - vowelArray[queries[idx][0]]
        return ans  
        