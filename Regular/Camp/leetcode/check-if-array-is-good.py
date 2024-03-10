class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if i != nums[i - 1]:
                return False
        if nums[-1] != len(nums) - 1:
            return False
        else:
            return True       