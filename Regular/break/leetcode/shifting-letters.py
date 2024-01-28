class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        pref = [0]*(len(s) + 1)

        for indx, amount in enumerate(shifts):
            pref[0] += amount
            pref[indx + 1] -= amount
        
        for indx in range(1, len(pref)):
            pref[indx] += pref[indx - 1]

        print(pref)
        ans = ""
        # print(pref_of_shifts)
        for i in range(len(s)):
            _ord = ord(s[i]) - ord('a')

            val = (_ord + pref[i]) % 26
            ans += chr(val + ord('a')) 

        return ans
