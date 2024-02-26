class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0 for _ in range(k)]
        self.mn = float("inf")
        def backtrack(indx,child):
            if indx >= len(cookies):
                self.mn = min(self.mn,max(child))
                return 
            if self.mn <= max(child):return


            for i in range(k):
                child[i] +=cookies[indx]
                backtrack(indx + 1,child)
                child[i] -=cookies[indx]

        backtrack(0,child)
        return self.mn
        