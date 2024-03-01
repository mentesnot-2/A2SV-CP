class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        ans = 0
        row_max = [0] * len(grid)
        col_max = [0] * len(grid)

        for i in range(len(grid)):
            row_max[i] = max(grid[i])


        for j in range(len(grid[0])):
            curr = float("-inf")
            for i in range(len(grid)):
                curr = max(curr,grid[i][j])
            col_max[j] = curr
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == row_max[i] or grid[i][j] == col_max[j]:
                    continue
                else:
                    rem = min(row_max[i],col_max[j])
                    val = rem - grid[i][j]
                    ans+=val
        
        return ans


        