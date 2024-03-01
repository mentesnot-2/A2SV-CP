class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])



        def find(r,c,indx,visited):
            
            if indx== len(word):
                return True
                       
            if r >= m or r < 0 or c >= n or c < 0 :
                return False

            if (r,c) in visited:
                return False
                
            if board[r][c] != word[indx]:
                return False
            
            visited.add((r,c))
            return find(r + 1,c,indx + 1,visited.copy()) or find(r,c + 1,indx + 1,visited.copy()) or find(r,c - 1,indx + 1,visited.copy()) or find(r - 1,c,indx + 1,visited.copy())
            
            
        
        for i in range(m):
            for j in range(n):
                if find(i,j,0,visited = set()):
                    return True
        return False

            
        