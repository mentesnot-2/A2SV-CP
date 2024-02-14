class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        target = 1
        ps = 0
        indx = 0
        patches = 0
        while target <= n:
            while indx < len(nums) and target >= nums[indx]:
                ps+=nums[indx]
                indx+=1
            if ps < target:
                patches+=1
                ps+=(target)
            target = ps + 1         
        return patches
            
                
