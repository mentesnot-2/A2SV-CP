class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        row = len(mat)
        col = len(mat[0])

        for i in range(row):
            for j in range(col):
                mp[i + j].append(mat[i][j])
        ans = []

        for i in mp:
            if i % 2 == 0:
                temp = mp[i][::-1]
                
                for i in temp:
                    ans.append(i)
            else:
                for j in mp[i]:
                    ans.append(j)
        return ans
        