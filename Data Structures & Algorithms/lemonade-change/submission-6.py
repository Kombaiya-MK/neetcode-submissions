class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        currentChange = 0
        changeToGive = 0

        for bill in bills:
            changeToGive = bill - 5
            print(currentChange)

            if (currentChange - changeToGive) < 0:
                return False

            currentChange += 5
            
        return True

        