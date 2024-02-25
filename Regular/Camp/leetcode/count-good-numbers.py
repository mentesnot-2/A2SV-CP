class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        def my_pow(base,exp):
            res = 1
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % mod
                base = (base * base) % mod
                exp//=2
            return res
            
        return (my_pow(5, (n + 1) // 2) * my_pow(4,n // 2)) % mod