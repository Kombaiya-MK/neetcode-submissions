class Solution:
    def getRow(self, n: int) -> List[int]:
        row = [1]

        for _ in range(n):
            row = [1] + [
                row[i - 1] + row[i]
                for i in range(1, len(row))
            ] + [1]

        return row