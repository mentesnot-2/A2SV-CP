class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = [str(i) for i in b]
        b = int("".join(b))
        def helper(x,n):
            if n == 0:
                return 1
            elif n % 2 == 0:
                res = helper(x,n // 2) % 1337
                return res ** 2
            elif n % 2 == 1:
                res = helper(x,n // 2) % 1337
                return x * (res ** 2)
        return helper(a,b) % 1337