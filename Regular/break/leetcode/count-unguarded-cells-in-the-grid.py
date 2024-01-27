class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0 for _ in range(n)] for _ in range(m)]

        for [i,j] in guards:
            mat[i][j] = 1
        for [i,j] in walls:
            mat[i][j] = -1
        
        def dfs(i,j,di):
            if i < 0 or i >= m or j < 0 or j >= n or mat[i][j] == 1 or mat[i][j] == -1:
                return 
            else:
                mat[i][j] = 2
            i = i + lst[di]
            j = j + lst[di + 1]
            dfs(i,j,di)
        lst = [1,0,-1,0,1]
        for [i,j] in guards:
            for indx in range(4):
                k = i + lst[indx]
                l = j + lst[indx + 1]
                dfs(k,l,indx)
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    count+=1
        return count

        