class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        l = 0
        s = list(s)
        for i in range(len(s)):
            if l < i  and s[l] == "1" and s[i] == "0":
                count+=( i - l)
                s[l],s[i] = s[i],s[l]
                l+=1
            while l < len(s) and s[l] == "0":
                l+=1
        return count
        