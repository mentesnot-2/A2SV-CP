class Solution:

    def backtrack(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in map(str, range(1, 10)):
                        if self.check_valid_grid(board, num, i, j):
                            board[i][j] = num
                            if self.backtrack(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def check_valid_grid(self, board, num, row, col):
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True

    def solveSudoku(self, board):
        self.backtrack(board)
