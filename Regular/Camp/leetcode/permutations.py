class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)


        def backtrack(indx):
            if indx == n:
                result.append(nums.copy())
                return 
            for i in range(indx,n):
                nums[indx],nums[i] = nums[i],nums[indx]
                backtrack(indx + 1)
                nums[indx],nums[i] = nums[i],nums[indx]
        backtrack(0)
        return result