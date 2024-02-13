class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirn = 'r'
        matrix = [[-1]*n for _ in range(n)]
        i = 0
        j = 0
        value = 1
        while value < (n ** 2 + 1):
            matrix[i][j] = value
            
            if dirn=='r':
                if j+1 >= n or matrix[i][j+1]!=-1:
                    dirn = 'd'
                    i += 1
                else:
                    j += 1

            elif dirn=='l':
                if j-1 < 0 or matrix[i][j-1]!=-1:
                    dirn = 'u'
                    i -= 1
                else:
                    j -= 1
                
            elif dirn=='u':
                if i-1 < 0 or matrix[i-1][j]!=-1:
                    dirn = 'r'
                    j += 1
                else:
                    i -= 1

            elif dirn=='d':
                if i+1 >= n or matrix[i+1][j]!=-1:
                    dirn = 'l'
                    j -= 1
                else:
                    i += 1
            value+=1
        return matrix