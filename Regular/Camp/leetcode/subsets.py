class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        ans = [[]]
        curr = []
        def backtrack(indx):
            if indx >= len(self.nums):
                return
            if len(curr) >= len(self.nums):
                return
            curr.append(nums[indx])
            ans.append(curr.copy())
            
            backtrack(indx+1)
            curr.pop()
            backtrack(indx + 1)
        backtrack(0)
        # ans.append([])
        return ans

        