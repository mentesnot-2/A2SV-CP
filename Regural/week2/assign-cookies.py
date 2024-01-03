class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ch,co = 0,0
        count = 0
        while ch < len(g):
            if co == len(s):
                return count
            elif g[ch] <= s[co]:
                count+=1
                ch+=1
                co+=1
            else:
                co+=1
        return count
        