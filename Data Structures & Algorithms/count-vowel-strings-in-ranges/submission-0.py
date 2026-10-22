class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = { 'a', 'e', 'i', 'o', 'u'}    
        vowelArray = [0] * (len(words) + 1)
        idx = 0
        for word in words:
            freq = {}
            for ch in word:
                if ch in vowels:
                    freq[ch] = freq.get(ch, 0) + 1
            
            vowelArray[idx + 1] = len(freq)
            idx += 1
        
        ans = []
        
        for idx in range(1, len(vowelArray)):
            vowelArray[idx] = vowelArray[idx - 1] + vowelArray[idx]
        # print(vowelArray)

        ans = [0] * len(queries)
        for idx in range(len(queries)):
            ans[idx] = vowelArray[queries[idx][1]+1] - vowelArray[queries[idx][0]]
        return ans  
        