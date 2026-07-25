class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        stack = []
        # position = position.sort()
        indices = sorted(range(len(position)), key=lambda i: position[i])
        for idx in range(len(indices) - 1, -1, -1):
            arrivalTime = (target - position[indices[idx]]) / speed[indices[idx]]
            # print(arrivalTime)
            if not stack or stack[-1] < arrivalTime:
                fleets += 1
                stack.append(arrivalTime)
        # print(stack)
        return fleets
        