class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = {}

        for word in s1.split(" "):
            freq[word] = freq.get(word, 0) + 1
        
        for word in s2.split(" "):
            if word in freq:
                freq[word] += 1
            
            else:
                freq[word] = 1
            

        ans = []

        for word in freq:
            if freq[word] == 1:
                ans.append(word)
        return ans

