class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # self.n = n
        def backtrack(k,curr,opn,clsd):
            if opn == clsd == k:
                
                ans.append("".join(curr))
                return
            if opn < n:
                curr.append("(")
                backtrack(k,curr,opn + 1,clsd)
                curr.pop()

            if clsd < opn:
                curr.append(")")
                backtrack(k,curr,opn,clsd + 1)
                curr.pop()
        backtrack(n,[],0,0)
        return ans

                
        