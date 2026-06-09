class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiagonal = set()
        negDiagonal = set()

        board = [["."] * n for i in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                copy = ["".join(i) for i in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (row + c) in posDiagonal or (row - c) in negDiagonal:
                    continue

                col.add(c)
                posDiagonal.add(row + c)
                negDiagonal.add(row - c)
                board[row][c] = "Q"

                backtrack(row + 1)

                col.remove(c)
                posDiagonal.remove(row + c)
                negDiagonal.remove(row - c)
                board[row][c] = "."

        backtrack(0)
        return res
