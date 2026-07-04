class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for idx in range(len(operations)):

            if operations[idx] == '+':
                newRecord = operations[idx - 1] + operations[idx - 2]
                stack.append(newRecord)
            
            elif operations[idx] == 'C':
                stack.pop(-1)
            
            elif operations[idx] == 'D':
                newRecord = int(operations[idx - 1]) * 2
                stack.append(newRecord)
            
            else:
                stack.append(operations[idx])
        print(stack)
        totalSum = 0

        for num in stack:
            totalSum += int(num)
        return totalSum
        