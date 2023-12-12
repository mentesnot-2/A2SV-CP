class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_set = set(nums)
        l = 0
        mx = 0
        for i in hash_set:
            if (i - 1) not in hash_set:
                l = 1
                while (i + 1) in hash_set:
                    l+=1
                    i+=1
                mx = max(mx,l)
        return mx

        


        