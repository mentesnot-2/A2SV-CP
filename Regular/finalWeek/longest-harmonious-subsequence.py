class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maxLen = 0

        for key in counter:
            if key + 1 in counter:
                maxLen = max(maxLen,counter[key] + counter[key + 1])
        return maxLen

