class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        comb = []
        def backtrack(i,sm):
            if i >= len(candidates):
                return
            if sm == target:
                ans.append(comb.copy())
                return
            if sm > target:
                return

            sm+=candidates[i]
            comb.append(candidates[i])

            backtrack(i,sm)

            sm-=candidates[i]
            comb.pop()

            backtrack(i + 1,sm)
        backtrack(0,0)
        return ans