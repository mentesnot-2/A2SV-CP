class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def check(md):
            sm = 0
            for num in nums:
                sm+=(math.ceil(num / md))
            return sm

        low,high = 1,max(nums)

        while low < high:
            md = low + (high - low) // 2

            if check(md) <= threshold:
                high = md
            else:
                low = md + 1
        return low
        