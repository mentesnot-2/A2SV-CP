class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        initial = sum(nums[:2 * k])

        for i in range(k,n - k):
            
            initial+=nums[i + k]
            avg = (initial) // ((2*k) + 1)
           
            ans[i] = avg
            initial-=nums[i - k]
        return ans
                