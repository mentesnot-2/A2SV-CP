class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = float("inf")
        tot = 0
        l = 0
        for i in range(len(nums)):
            tot+=nums[i]
            while tot >= target:
                size = min(size,i - l + 1)
                tot-=nums[l]
                l+=1
        return size if size != float("inf") else 0

        