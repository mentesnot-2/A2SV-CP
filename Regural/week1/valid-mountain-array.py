class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        nums = arr
        cnt = 0 
        for i in range(1,len(nums) - 1):
            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                return False
            if nums[i] == nums[i- 1] or nums[i] == nums[i + 1]:
                return False
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                cnt+=1
        if cnt != 0 and nums[-1] > nums[-2]:
            cnt+=1
        return cnt == 1

        