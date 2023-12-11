class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        even_sum = 0
        ans = [] 
        for i in nums:
            if i % 2 == 0:
                even_sum+=i
        for val,index in queries:
            if nums[index] % 2 == 0:
                even_sum-=nums[index]
            nums[index] = nums[index] + val

            if nums[index] % 2 == 0:
                even_sum+=nums[index]
            ans.append(even_sum)    
        return ans        

        