class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        operation = 0
        for i in range(n -2,-1,-1):
            if nums[i] > nums[i + 1]:
                rem = nums[i] / nums[i + 1]
                if rem % 2 != 0:
                    space = math.ceil(nums[i] / nums[i + 1])
                    val = nums[i] // space
                    nums[i] = val
                    operation+=(space - 1)
                    
                else:
                    space = math.ceil(nums[i] / nums[i + 1])
                    val = nums[i] // space
                    operation+=(space - 1)
                    nums[i] = val
                    
        return operation