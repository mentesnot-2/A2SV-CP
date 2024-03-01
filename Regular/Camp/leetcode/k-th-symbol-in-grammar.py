class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        size = 2 ** (n - 2)
        if k > size :
            k = k  % size
            if k == 0:
                k = size
            return 1 - self.kthGrammar(n - 1,k)

        return self.kthGrammar(n - 1,k)

            