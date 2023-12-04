class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for i in range(len(nums)-1):
            if i % 2 == 0:
                ans =  ans + [nums[i + 1]] * nums[i]
        return ans
        