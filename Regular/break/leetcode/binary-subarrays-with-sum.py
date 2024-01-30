class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = [nums[0]]
        pref_map = defaultdict(int)
        for i in range(len(nums)):
            pref.append(pref[-1] + nums[i])

        count = 0
        for i in range(len(pref)):
            if pref[i] - goal in pref_map:
                count+=pref_map[pref[i] - goal]
            pref_map[pref[i]]+=1
        return count