class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        directions = {'N':1, 'S':-1, 'E':2, 'W':-2}
        distance = 0
        visited.add(0)
        for point in path:
            distance += directions[point]
            if distance in visited:
                return True
            visited.add(distance)
        return False
        