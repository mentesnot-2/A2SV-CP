class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,  key = lambda x:x[1])
        arrow=1
        ends=points[0][1]
        N=len(points)
        for j in range(1,N):
            if points[j][0]<=ends:
                continue
            else:
                arrow+=1
                ends=points[j][1]
        return arrow