class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref = [0]*(len(s) + 1)

        for shift in shifts:
            start,end,dirn = shift
            if dirn == 1:
                pref[start] += 1
                pref[end + 1] -= 1
            else:
                pref[start] -= 1
                pref[end + 1] += 1
        for indx in range(1, len(pref)):
            pref[indx] += pref[indx - 1]

        ans = ""
        
        for i in range(len(s)):
            _ord = ord(s[i]) - ord('a')

            val = (_ord + pref[i]) % 26
            ans += chr(val + ord('a')) 

        return ans
