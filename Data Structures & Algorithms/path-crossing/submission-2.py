from collections import defaultdict
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = defaultdict(list)
        directions = defaultdict(list)
        directions = {'N':(1, 0), 'S':(-1, 0), 'E':(0, -1), 'W':(0, 1)}
        visited = {(0, 0):1}
        distance = [0, 0]
        for point in path:
            distance[0] += directions[point][0]
            distance[1] += directions[point][-1]
            if (distance[0], distance[1]) in visited:
                return True
            visited[(distance[0], distance[1])] = 1
        return False
        