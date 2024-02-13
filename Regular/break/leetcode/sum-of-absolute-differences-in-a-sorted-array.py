class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = [0]
        n = len(nums)
        ans =  []
        for i in range(len(nums)):
            pref.append(pref[-1] + nums[i])

        suffix = []

        for i in range(len(nums)):
            suffix.append(pref[-1] - pref[i + 1]) 
        print("pref",pref,"suff",suffix)
        for i in range(len(nums)):
            ans.append(nums[i] * i - pref[i] + suffix[i] - nums[i] * (n - i -1) )
        return ans 