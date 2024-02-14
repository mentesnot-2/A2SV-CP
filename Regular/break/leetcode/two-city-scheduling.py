class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        count=0
        val=[]
        for i in range(len(costs)):
            count+=costs[i][0]
            val.append(costs[i][1]-costs[i][0])
        val.sort()
        for i in range(len(costs)//2):
            count+=val[i]
        return count
        
