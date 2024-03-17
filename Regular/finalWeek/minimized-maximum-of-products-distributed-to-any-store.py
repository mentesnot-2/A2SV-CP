class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def check(md):
            res = 0
            for quantity in quantities:
                res+=(math.ceil(quantity / md))
            return res
        low,high = 1,max(quantities)

        while low < high:
            md = low + (high - low) // 2
            if check(md) <= n:
                high = md
            else:
                low = md + 1
                
        return low


        