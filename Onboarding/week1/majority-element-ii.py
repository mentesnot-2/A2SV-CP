class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        val={}
        n=len(nums)
        for i in nums:
            if i in val:
                val[i]+=1
            else:
                val[i]=1
        lst=[]
        for k in val:
            if val[k]>n//3:
                lst.append(k)
        return lst