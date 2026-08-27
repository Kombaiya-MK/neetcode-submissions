class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        ansStr = ""

        for digit in digits:
            ansStr += str(digit)
        
        ansStr = str(int(ansStr) + 1)

        print(ansStr)

        ans = []

        for ch in ansStr:
            ans.append(int(ch))
        
        return ans

        