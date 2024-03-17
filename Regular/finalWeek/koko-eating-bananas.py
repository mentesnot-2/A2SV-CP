class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def check(md):
            hr = 0
            for i in piles:
                hr+=math.ceil(i/md)
            return hr
        low,high = 1,max(piles)

        while low < high:
            md = low + (high - low) // 2

            if check(md) <= h:
                high = md
            else:
                low = md + 1
        return low
        