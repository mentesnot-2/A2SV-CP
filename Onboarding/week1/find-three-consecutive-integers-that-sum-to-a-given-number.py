class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        temp = num - 3

        if temp % 3 != 0:
            return []
        else:
            return [temp // 3, (temp // 3) + 1, (temp // 3) + 2]
        