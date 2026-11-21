class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        n = len(nums)
        # print(freq)
        maxNum, maxFreq = 0, 0
        
        for key in freq:
            if freq[key] > maxFreq:
                maxFreq = freq[key]
                maxNum = key
        # print(maxNum, maxFreq)
        
        currentFreq = 0
        for idx in range(n):        
            left = idx + 1
            right = n - idx - 1
        
            if nums[idx] == maxNum:
                currentFreq += 1
                maxFreq -= 1
            
            if currentFreq > (left // 2) and maxFreq > (right // 2):
                return idx

            
            # print(left, right, maxFreq, currentFreq)

        return -1