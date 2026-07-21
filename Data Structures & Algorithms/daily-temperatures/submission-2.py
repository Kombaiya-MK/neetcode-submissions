class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for idx in range(n):
            # print(stack)
            while stack and stack[-1][0] < temperatures[idx]:
                prevIndex = stack.pop()
                print(prevIndex)
                result[prevIndex[-1]] = idx - prevIndex[-1]
            stack.append([temperatures[idx], idx])
        return result
        