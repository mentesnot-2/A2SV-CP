class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sm = 0
        left = 0
        mx = float("-inf")
        mp = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in mp:
                mx =  max(mx,sm)  
                while left <= mp[nums[i]]:
                    sm-=nums[left]
                    left+=1
            sm+=nums[i]
            mp[nums[i]] = i
            print(sm)
            print(mx)
        return mx if (mx != float("-inf") and mx > sm) else sm 