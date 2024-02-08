class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pref = [0] * n
        for a,b in requests:
            pref[a]+=1
            if b != n - 1:
                pref[b + 1]-=1
        for i in range(1, n):
            pref[i] += pref[i - 1]
        pref.sort(reverse=True)
        nums.sort(reverse=True)
        ans = 0
        for i in range(n):
            ans+=pref[i] * nums[i]
        mod = 10**9 + 7
        return ans % mod