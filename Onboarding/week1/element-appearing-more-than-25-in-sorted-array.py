class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        mx = 0
        n = len(arr)
        l = 0
        el = arr[0]
        for i in range(n):
            if arr[i] != arr[l]:
                l = i
            if i - l + 1 > mx:
                mx = i - l + 1
                el = arr[i]
        return el