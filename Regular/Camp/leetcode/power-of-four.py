class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n%4!=0 or n<=0:
            return False
        else:
            n=n//4
            return self.isPowerOfFour(n)