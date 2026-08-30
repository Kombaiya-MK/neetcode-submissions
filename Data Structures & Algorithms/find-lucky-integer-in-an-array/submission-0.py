class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        maxNum = -1
        for key in freq:
            if key == freq[key]:
                maxNum = max(maxNum, key)
        return maxNum
        