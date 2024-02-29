class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal=[]
        for i in range(rowIndex+1):
            if len(pascal)==0:
                pascal.append([1])
            elif len(pascal)==1:
                pascal.append([1,1])
            else:
                lst=[]
                lst.append(1)
                k=1
                m=0
                end=pascal[-1]
                while k<len(end):
                    lst.append(end[m]+end[k])
                    m+=1
                    k+=1
                lst.append(1)
                pascal.append(lst)
        
        return pascal[-1]
        