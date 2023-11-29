class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        el = matrix[0][0]
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1,m):
            for j in range(1,n):
                
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True

        