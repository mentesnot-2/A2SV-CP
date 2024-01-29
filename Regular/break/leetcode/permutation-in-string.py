class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dictP=Counter(s1)
        dictS={}
        l=0
        
        for r in range(len(s2)):
            dictS[s2[r]]=dictS.get(s2[r],0)+1
            if (r-l+1)==len(s1):
                if dictS==dictP:
                    return True
                dictS[s2[l]]-=1
                if dictS[s2[l]]==0:
                    dictS.pop(s2[l])   
                l+=1
        # return 