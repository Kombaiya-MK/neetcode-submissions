class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        stack = []

        for idx in range(len(digits) - 1, -1 , -1):
            curSum = digits[idx] + carry
            digit = curSum % 10
            carry = curSum // 10
            stack.append(digit)
        
        if carry > 0:
            stack.append(carry)
         
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans