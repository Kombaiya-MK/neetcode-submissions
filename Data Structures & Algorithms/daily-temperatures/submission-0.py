class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        Map = {}

        for idx in range(n):
            print(stack)
            while stack and stack[-1][0] < temperatures[idx]:
                prev = stack.pop()
                Map[prev[0]] = idx - prev[-1]
            stack.append([temperatures[idx], idx])
        return [Map.get(temp, 0) for temp in temperatures]
        