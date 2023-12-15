class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        mx = 1
        sm = nums[0]
        l = 0
        for i in range(1,n):
            sm+=nums[i]
            ans = nums[i]
            while sm + k < ans * (i - l + 1):
                sm-=nums[l]
                l+=1
            mx = max(mx,i - l + 1)
        return mx



        