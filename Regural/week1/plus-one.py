class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=''
        for i in digits:
            res=res + str(i)
        res=int(res) + 1
        res=str(res)
        lst=[]
        for i in range(len(res)):
            lst.append(int(res[i]))
        return lst