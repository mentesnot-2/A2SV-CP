class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        
        ans = 0
        l = 0
        rplc = {}
        maxf = 0
        for r in range(len(s)):
            rplc[s[r]] = 1 + rplc.get(s[r],0)
            maxf = max(maxf,rplc[s[r]])
            
            if (r - l + 1) - maxf > k:
                rplc[s[l]]-=1
                l+=1
            ans = max(ans,r - l + 1)
        return ans
        
            
            
        