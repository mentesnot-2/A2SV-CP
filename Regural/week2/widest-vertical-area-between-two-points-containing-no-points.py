class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x= sorted(list(zip(*points))[0])
        return max([x[i+1]-x[i] for i in range(len(x)-1)])
        