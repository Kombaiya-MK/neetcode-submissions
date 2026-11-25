class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        numMap = [0] * (2**k)
        
        def ConvertToDecimal(bin):
            val = 0
            
            for idx in range(k):
                val += int(bin[idx]) * (2 ** (k - idx - 1))
                # print(val)
            numMap[val] = 1
        n = len(s)
        
        for right in range(n - k + 1):
            # print(s[right : right + k])
            ConvertToDecimal(s[right: right + k])
        return sum(numMap) == len(numMap)
        