class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        indx = bisect.bisect_left(nums,target)

        if nums[indx - 1] < target:
            return indx
        else:
            return indx
        