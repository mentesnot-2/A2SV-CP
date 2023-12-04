class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                l = i + 1
            else:
                ans = max(ans,i - l + 1)
        return ans
