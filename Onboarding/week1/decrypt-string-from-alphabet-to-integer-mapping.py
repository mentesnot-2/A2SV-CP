class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        i = 0
        n = len(s)
        while i < n:
            if i + 2 < n and s[i + 2] == "#":
                ans +=chr(int(s[i:i + 2]) + ord('a') - 1)
                i+=3
            else:
                ans+=chr(int(s[i]) + ord('a' )- 1)
                i+=1
        return ans



        