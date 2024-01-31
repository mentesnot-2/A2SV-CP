class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                
        pref = [0]
        
        for m in range(len(nums)):
            pref.append(pref[-1] + nums[m])
        
            
        dct = {}
        ans = 0
        for j in range(len(pref)):
            if (pref[j] - k) in dct:
                ans+=dct[pref[j] - k]
                
            if pref[j] not in dct:
                dct[pref[j]] = 0
            dct[pref[j]]+=1
           
        return ans
            