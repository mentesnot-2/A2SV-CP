class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = s.split(" ")
        
        mx = 0
        for j in range(len(s)):
            mx = max(mx,len(s[j]))
        ans = [""] * mx
        for i in range(mx):
            val = ""
            for j in range(len(s)):

                if len(s[j]) <= i:
                    val+=" "
                else:
                    val+=s[j][i]
            val = val.rstrip()
            ans[i] =  val
        
        return ans
        