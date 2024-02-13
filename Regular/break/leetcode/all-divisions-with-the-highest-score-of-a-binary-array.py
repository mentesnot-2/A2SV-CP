class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        pref = [0]

        for i in range(len(nums)):
            pref.append(pref[-1] + nums[i])

        ans = []
        mx = float("-inf")
        for i in range(len(pref)):
            curr = i - pref[i] + pref[-1] - pref[i]
            if curr == mx:
                ans.append(i)
            elif curr > mx:
                ans = [i]
                mx = curr
        return ans