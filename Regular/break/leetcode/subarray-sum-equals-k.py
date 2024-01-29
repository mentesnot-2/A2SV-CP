class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref=[0]
        for i in range(len(nums)):
            pref.append(pref[-1]+nums[i])
        freq={}
        count=0
        for i in range(len(pref)):
            if (pref[i]-k) in freq:
                count+=freq[(pref[i]-k)]
            if pref[i] not in freq:
                freq[pref[i]]=0
            freq[pref[i]]+=1
        return count