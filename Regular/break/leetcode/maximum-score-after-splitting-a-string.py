class Solution:
    def maxScore(self, s: str) -> int:
        pref = [int(s[0])]

        count1 = 0
        if s[0] == "1":
            count1 = 1

        for i in range(1,len(s)):
            pref.append(pref[-1] + int(s[i]))
        ans = float("-inf")

        for i in range(len(pref) - 1):
        
            ans = max(ans,(i - pref[i]) + (pref[-1] - pref[i]) + 1)
        return ans



        
        