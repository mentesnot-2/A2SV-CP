class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sm = sum(nums[:3])
        nums.sort()
        
        for i in range(len(nums)):
            l,r = i + 1,len(nums) - 1
            
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                
                if abs(threeSum - target) < abs(sm-target):
                    sm = threeSum
                if threeSum < target:
                    l+=1
                elif threeSum > target:
                    r-=1
                else:
                    return sm
        return sm