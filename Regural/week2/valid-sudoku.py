class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in square[i//3,j//3]):
                    return False
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                square[i//3,j//3].add(board[i][j])
        return True

        