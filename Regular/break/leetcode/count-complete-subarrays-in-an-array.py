class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        mp_1 = Counter(nums)
        left = 0
        mp_2 = defaultdict(int)
        count = 0
        ln = len(nums) - 1
        for i in range(len(nums)):
            mp_2[nums[i]]+=1
          
            while len(mp_2) == len(mp_1):
                count+=(ln - i) + 1
                mp_2[nums[left]]-=1
                if mp_2[nums[left]] == 0:
                    del mp_2[nums[left]]
                left+=1
        return count