class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        def count(num):
            bits = 0
            
            while num:
                if num & 1:
                    bits += 1
                num >>= 1
            
            return bits

        for num in range(n+1):
            ans.append(count(num))
        return ans

        