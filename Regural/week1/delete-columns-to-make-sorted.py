class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lenstr=len(strs)
        lenele=len(strs[0])
        count=0
        for i in range(lenele):
            for j in range(lenstr-1):
                if strs[j][i]>strs[j+1][i]:
                    count+=1
                    break
        return count