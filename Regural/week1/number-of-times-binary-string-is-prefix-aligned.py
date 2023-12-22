class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        mx_index = 0
        cnt = 0
        for i in range(len(flips)):
            if flips[i] >= mx_index:
                mx_index = flips[i]
            if mx_index == i+ 1:
                cnt+=1
        return cnt
                
        