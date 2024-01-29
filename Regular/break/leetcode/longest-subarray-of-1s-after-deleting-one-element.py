class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        hashmap = {x: 0 for x in nums}
        length = 0
        if 0 not in hashmap.keys():
            return len(nums) - 1
        for r in range(len(nums)):
            hashmap[nums[r]] += 1
            if hashmap[0] > 1:
                hashmap[nums[l]] -= 1
                l += 1
            length = max(length, r - l)
        return (length)
        