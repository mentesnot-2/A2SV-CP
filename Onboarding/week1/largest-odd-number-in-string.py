class Solution(object):
    def largestOddNumber(self, num):
        i = len(num) - 1
        S = {'0','2','4','6','8'}
        while i >= 0 and num[i] in S:
            i -= 1
        return num[:i + 1]

        


        
        