class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        
        def backtrack(candidate):
            if len(path) == k:
                ans.append(path.copy())
                return

            for next_cand in range(candidate + 1, n + 1):
                path.append(next_cand)
                backtrack(next_cand)
                path.pop()
        backtrack(0)
        return ans
        