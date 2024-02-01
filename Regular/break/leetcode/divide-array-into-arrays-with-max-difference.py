class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums):
            curr = []
            j = i
            while i < len(nums) and i < j + 3:
                curr.append(nums[i])
                i+=1
            if curr[-1] - curr[0] > k:
                return []
            else:
                ans.append(curr)
        return ans
            
        