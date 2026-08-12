class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        maxElement = 0
        minElement = float('inf')

        for val in freq:
            if freq[val] & 1:
                maxElement = max(maxElement, freq[val])
            else:
                minElement = min(minElement, freq[val])
        print(maxElement, minElement)
        return abs(maxElement - minElement)
        