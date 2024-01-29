class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        prefix=[0] + list(itertools.accumulate(nums))
        
        freq={}
        for i in prefix:
            if i%k in freq:
                count+=freq[i%k]
               
            elif i%k not in freq:
                freq[i%k]=0
            freq[i%k]+=1
        return count
        