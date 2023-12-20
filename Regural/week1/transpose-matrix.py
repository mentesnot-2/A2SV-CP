class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        trans_mat = [ [0 for y in range(len(matrix))] for y in range(len(matrix[0]))] 
        # print(trans_mat)

        for row in range(len(matrix)):

            for col in range(len(matrix[0])):

                trans_mat[col][row] = matrix[row][col]

        return trans_mat


        