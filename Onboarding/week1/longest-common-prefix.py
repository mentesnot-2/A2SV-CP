class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """ 
        ln = []
        for i in strs:
            ln.append(len(i))
        mn = min(ln)
        ans = ""
        for i in range(mn):
            curr = strs[0][i]

            
            for j in range(0,len(strs)):
                # if j == len(strs) or (strs[j] and strs[i]) and strs[j][i]:
                
                if strs[j][i] != curr:
                    return ans
                

            ans+=strs[0][i]
            
           
        return ans
        