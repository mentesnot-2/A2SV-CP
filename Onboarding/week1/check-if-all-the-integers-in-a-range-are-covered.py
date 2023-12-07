class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        tot = set()
        for x,y in ranges:
            for i in range(x,y+1):
                tot.add(i)
        tot2 = {item for item in range(left,right + 1)}

        return tot2 <= tot