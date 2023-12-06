class Solution:
    def totalMoney(self, n: int) -> int:
        num_monday = n // 7

        initVal = 28
        if n <= 7:
            return (n*(n + 1))// 2

        prev = initVal
        for i in range(1, num_monday):
            initVal = initVal + (prev + 7)
            prev = prev + 7
        
        if n > num_monday*7:
            val = num_monday + 1
            m = n - (num_monday*7)
            for i in range(0, m):
                initVal += (val + i)
            # initVal += val
        
        return initVal