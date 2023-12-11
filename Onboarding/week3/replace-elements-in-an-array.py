class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        mp = {}
        for indx,val in enumerate(nums):
            mp[val] = indx
       
        n = len(nums)
        
        for x,y in operations:
            if x in mp:
                nums[mp[x]] = y
                mp[y] = mp[x]

        return nums


        