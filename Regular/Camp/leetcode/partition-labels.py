class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i,c in enumerate(s)}
        j = k = 0
        final = []
        for indx,val in enumerate(s):
            j = max(j,last[val])
            if indx == j:
                final.append(indx - k + 1)
                k = indx + 1
        return final
                
        