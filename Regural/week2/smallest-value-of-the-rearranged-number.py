class Solution:
    def smallestNumber(self, num: int) -> int:
        flag = False
        if num < 0:
           flag = True
        
        nums = str(num)[1:] if flag else str(num)
        nums = [i for i in nums]
        nums.sort()
        ans = ''
        if flag:
            ans = "-" + "".join(nums)[::-1]
            return int(ans)
        i = 0
        while i < len(nums) and nums[i] == "0":
            i+=1
        if i < len(nums):
            nums[0],nums[i] = nums[i],nums[0]
        return int("".join(nums))

        