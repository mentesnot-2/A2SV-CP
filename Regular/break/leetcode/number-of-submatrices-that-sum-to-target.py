class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        pref = []
        row,col = len(matrix),len(matrix[0])
        for j in range(row):
            curr = []
            for i in range(col):
                if i == 0:
                    curr.append(matrix[j][i])
                else:
                    curr.append(curr[-1] + matrix[j][i])
            pref.append(curr)
        
        ans = 0
        
        for i in range(len(pref[0])):
            for k in range(i,len(pref[0])):
                mp = defaultdict(int)
                mp[0] = 1
                curr_sum = 0
                for j in range(len(pref)):
                    curr_sum+=pref[j][k]
                    if i > 0:
                        curr_sum-=pref[j][i - 1]
                   
                    ans+=(mp[curr_sum - target])
                    
                    mp[curr_sum] +=1
            
        return ans

        

