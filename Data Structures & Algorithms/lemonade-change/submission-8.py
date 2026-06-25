class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        currentChange = 0
        changeToGive = 0

        for bill in bills:
            currentChange += 5
            changeToGive = bill - 5
            currentChange -= changeToGive
            print(currentChange)

            if (currentChange) < 0:
                return False
        return True

        