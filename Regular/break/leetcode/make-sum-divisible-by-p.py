class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        n = len(nums)
        ln = n
        _dict = {0:-1}
        
        curr_sum = 0
        if target == 0:
            return 0

        for i in range(n):
            curr_sum+=nums[i]
            key = curr_sum % p -target

            if key < 0:
                key+=p
            if key in _dict:
                ln = min(ln,i - _dict[key])
            _dict[curr_sum % p] = i
        
        return ln if ln < n  else -1


