class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        n = len(nums)
        for i in cntr:
            if cntr[i] >= n / 2:
                return i
        