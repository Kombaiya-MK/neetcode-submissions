class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}

        for ch in chars:
            freq[ch] = freq.get(ch, 0) + 1

        def isContains(word):
            wordFreq = {}
            for ch in word:
                if ch not in freq:
                    return False
                wordFreq[ch] = wordFreq.get(ch, 0) + 1

                if wordFreq[ch] > freq[ch]:
                    return False
            return True

        count = 0

        for word in words:
            if isContains(word):
                count += len(word)
        return count
                
        