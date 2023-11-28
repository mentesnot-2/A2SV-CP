class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nm = 0
        temp = x
        while x > 0:
            nm = nm * 10 + (x % 10)
            x = x // 10
        print(nm)
        return nm == temp