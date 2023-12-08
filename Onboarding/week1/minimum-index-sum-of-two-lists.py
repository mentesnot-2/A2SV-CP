class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash={}
        great=[]
        val=float("inf")
        for i in range(len(list1)):
            hash[list1[i]]=i
        for i in range(len(list2)):
            if list2[i] in hash:
                if hash[list2[i]]+i==val:
                    great.append(list2[i])
                if hash[list2[i]]+i<val:
                    great.clear()
                    great.append(list2[i])
                val=min(val,hash[list2[i]]+i)
        return great

            
            
        