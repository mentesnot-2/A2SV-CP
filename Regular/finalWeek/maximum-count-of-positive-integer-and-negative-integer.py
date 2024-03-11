class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        ans = 0
        res = 0
        flag = False
        for i in range(len(nums)):
            if nums[i] < 0:
                ans+=1
            elif nums[i] == 0:
                continue
            else:
                res = i
                flag = True
                break
        # print(ans,res)
        if ans == 0 and not flag:
            return 0
        elif not flag:
            return ans
        else:
            return max(ans,len(nums) - res)


