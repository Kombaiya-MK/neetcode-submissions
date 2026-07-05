class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = {}
        cols = {}
        boxes = {}


        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue

                row = r
                col = c

                if row not in rows:
                    rows[row] = set()
                if col not in cols:
                    cols[col] = set()
                if board[r][c] in rows[row] or board[r][c] in cols[col]:
                    return False

                box = (r // 3) * 3 + (c // 3)

                if box not in boxes:
                    boxes[box] = set()

                if board[r][c] in boxes[box]:
                    return False
                rows[row].add(board[r][c])
                cols[col].add(board[r][c])
                boxes[box].add(board[r][c])
        return True
