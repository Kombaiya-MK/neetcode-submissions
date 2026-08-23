class Solution:
    def isHappy(self, n: int) -> bool:
        sumOfDigits = 0
        while n > 0:
            remainder = n % 10
            sumOfDigits += remainder * remainder
            n //= 10
        return sumOfDigits == 1


        