class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos =[]
        res = []
        
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        for k in range(len(pos)):
            res.append(pos[k])
            res.append(neg[k])
        return res