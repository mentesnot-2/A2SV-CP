class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match={}
        for index,num in enumerate(nums):
            if target-num in match:
                return [match[target- num], index]
            else:
                match[num] = index
        return []