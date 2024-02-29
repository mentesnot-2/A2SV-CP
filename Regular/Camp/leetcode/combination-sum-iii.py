class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        comb = []
        self.sum = 0
        def backtrack(num):
            if len(comb) == k and self.sum == n:
                self.ans.append(comb.copy())
                return
            if len(comb) == k:
                return
            if num > 9:return
            self.sum+=num
            comb.append(num)
            backtrack(num + 1)
            self.sum-=num
            comb.pop()
            backtrack(num + 1)
        backtrack(1)
        return self.ans

 
            
        