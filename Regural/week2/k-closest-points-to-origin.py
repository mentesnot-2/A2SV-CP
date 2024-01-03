import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tupl=[]
        for i in points:
            dst=sqrt((i[1]**2) + (i[0]**2))
            tupl.append([i,dst])
        sorted_tupl=sorted(tupl, key=lambda x: x[1])
        lst=[]
        for i in range(k):
            lst.append(sorted_tupl[i][0])
        return lst













        # dist=[]
        # for i, j in tupl:
        #     dist.append(j)
        # dist.sort()
        # # close=dist[k-1]
        # lst=[]
        # for m in range(k):
        #     for i, j in tupl:
        #         if dist[m]==j:
        #             if i not in lst:
        #                 lst.append(i)
        # return lst