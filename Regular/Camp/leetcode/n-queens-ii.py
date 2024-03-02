class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."] * n for _ in range(n)]
        col = [0] * n
        diag = [0] * (2 * n)
        oppDiagn = [0] * (2 * n)
        ans = []
        def backtrack(row):
            if row == n:
                ans.append(["".join(curr_state) for curr_state in board])
            for c in range(n):
                if col[c] + diag[row + c] + oppDiagn[n - row + c] == 0:
                    board[row][c] = "Q"
                    col[c] = diag[c  + row] = oppDiagn[n - row + c] = 1
                    backtrack(row + 1)
                    col[c] = diag[c  + row] = oppDiagn[n - row + c] = 0
                    board[row][c] = "."
            
        backtrack(0)
        return len(ans)