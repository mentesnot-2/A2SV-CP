class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if sum(nums[1:])==0:
            return 0
        elif sum(nums[1:])!=0:
            total=0
            for i in nums:
                total+=i
            res=nums[0]
            for j in range(1,len(nums)):
                if res==total-res-nums[j]:
                    return j
                else:
                    res+=nums[j]
        # elif sum(nums[:len(nums)-1])==0:
        #     return len(nums)-1
        # else:
        return -1