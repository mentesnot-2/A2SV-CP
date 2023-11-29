class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: 
        """
        if n == 0:
            return '0'  # Special case for 0
    
        result = ''
        while n > 0:
            remainder = n % 3
            result = str(remainder) + result
            n //= 3
        return '2' not in result

        
        