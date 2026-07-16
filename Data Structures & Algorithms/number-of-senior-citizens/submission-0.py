class Solution:
    def countSeniors(self, details: List[str]) -> int:
        maxCount = 0
        k = 11
        for i in range(len(details)):
            age = details[i][k:k+2]
            if int(age) > 60:
                maxCount += 1
        return maxCount

        