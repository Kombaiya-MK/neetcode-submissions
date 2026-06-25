class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        currentChange = 0

        for bill in bills:
            currentChange += 5 - (bill - 5)

            if currentChange < 0:
                return False
        return True

        