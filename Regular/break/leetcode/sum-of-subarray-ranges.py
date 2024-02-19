class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            min_elmnt = nums[i]
            mx_elmnt = nums[i]
            for j in range(i,n):
                if nums[j] < min_elmnt:
                    min_elmnt = nums[j]
                if nums[j] > mx_elmnt:
                    mx_elmnt = nums[j]
                
                ans+=(mx_elmnt  - min_elmnt)
        return ans
