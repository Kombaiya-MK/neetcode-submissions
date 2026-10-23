class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        totalWaitingTime = 0
        runningTime = customers[0][0]
        totalSum = 0
        for customer in customers:
            # print(customer[0], customer[1])
            runningTime = max(customer[0] + customer[1], runningTime + customer[1])
            totalWaitingTime = runningTime - customer[0]
            print(runningTime, customer[0], totalWaitingTime)
            totalSum += totalWaitingTime
        return totalSum / n
        