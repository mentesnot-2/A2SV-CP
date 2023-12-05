class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        val = n
        cnt = 0
        while n >= 2:
            cnt += n // 2
            n = ceil(n / 2)
        cnt = int(cnt)
        return cnt if val % 2 == 0 else cnt + 1
        