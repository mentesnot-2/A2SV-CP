class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        unique = set()
        both_same = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}
        
        for i in range(len(fronts)):
            if fronts[i] not in both_same:
                unique.add(fronts[i])
            if backs[i] not in both_same:
                unique.add(backs[i])
        mn = float("inf")
        for i in unique:
            mn = min(mn,i)
            print(i,mn)
        return mn if mn != float("inf") else 0