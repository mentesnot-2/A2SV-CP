class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pref = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                
                self.pref[row + 1][col + 1] = self.pref[row + 1][col] + self.pref[row][col + 1] - self.pref[row][col] + matrix[row][col]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.pref[row2 + 1][col2 + 1] - self.pref[row2 + 1][col1] - self.pref[row1][col2+1] + self.pref[row1][col1]
        
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)