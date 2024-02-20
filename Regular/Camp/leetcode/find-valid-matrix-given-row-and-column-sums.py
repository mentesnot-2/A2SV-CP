class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]

        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                curr = min(rowSum[i],colSum[j])
                matrix[i][j] = curr
                rowSum[i] -=curr
                colSum[j] -=curr
        return matrix