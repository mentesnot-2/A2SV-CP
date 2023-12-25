class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        tot=0
        res=0
        for i in range(len(mat)):
            tot+=mat[i][i]
            res+=mat[i][len(mat)-i-1]
        if len(mat)%2==0:
            return tot+res
        else:
            return tot+res-mat[(len(mat)//2)][(len(mat)//2)]