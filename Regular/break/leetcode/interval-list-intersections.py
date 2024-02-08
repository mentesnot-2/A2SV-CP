class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        for x,y in firstList:
            for i,j in secondList:
                if x > j or i > y:
                    continue
                ans.append([max(x,i),min(y,j)])
        return ans
        