class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,1
        ans = 0
        while j < len(nums):
            ans+=min(nums[i],nums[j])
            j+=2
            i+=2
        return ans
        