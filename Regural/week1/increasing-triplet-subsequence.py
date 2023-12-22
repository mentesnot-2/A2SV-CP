class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first,second = float("inf"),float("inf")

        for i in range(len(nums)):
            cur = nums[i]
            if cur <= first:
                first = cur
            elif cur <= second:
                second = cur
            else:
                return True
        return False