class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 0
        n = len(nums)
        for i in range(n - 2,-1,-1):
            if nums[i] > steps:
                steps = 0
                continue
            else:
                steps+=1
        if steps == 0:
            return True
        else:
            return False
        