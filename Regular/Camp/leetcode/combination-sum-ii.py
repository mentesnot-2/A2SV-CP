class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        comb = []
        
        def backtrack(indx,sm):
            if sm == target:
                ans.append(comb.copy())
                return
            if sm > target:
                return
            if indx >= len(candidates):
                return
            
            prev = -1
            for i in range(indx,len(candidates)):
                if candidates[i] == prev:
                    continue
                sm+=candidates[i]
                comb.append(candidates[i])
                backtrack(i + 1,sm)
                sm-=candidates[i]
                comb.pop()
                prev = candidates[i]
            
        backtrack(0,0)
        print(ans)
        return list(ans)