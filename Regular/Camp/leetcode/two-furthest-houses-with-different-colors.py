class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l=0
        r=len(colors)-1
        res=0
        while l<len(colors):
            while r>l:
                if colors[l]==colors[r]:
                    r-=1
                elif colors[l]!=colors[r]:
                    res=max(res,r-l)
                    break
            l+=1
            r=len(colors)-1
        return res
        