class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0 for _ in range(len(s) + 1)]
        for shift in shifts:
            l, r, dr = shift
            prefix[l] +=(1 if dr == 1 else -1)

            prefix[r + 1]-=(1 if dr == 1 else -1)


            

        pref = [prefix[0]]
        for i in range(1,len(prefix)):
            pref.append(pref[-1] + prefix[i])
        
        
        ans = []
        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            curr+=pref[i]
            curr %=26
            curr+=(ord("a"))
            ans.append(chr(curr))
        return "".join(ans)