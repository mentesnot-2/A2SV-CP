class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        mp = {}

        for i in cpdomains:
            val = i.split(" ")
            num = int(val[0])
            dmn = val[-1].split(".")
            if val[-1] not in mp:
                mp[val[-1]] = 0
            if dmn[-2] + "."+dmn[-1] not in mp:
                mp[dmn[-2] + "."+dmn[-1]] = 0
            if dmn[-1] not in mp:
                mp[dmn[-1]] = 0
            mp[val[-1]]+=int(num)
            if val[-1] != dmn[-2] + "."+dmn[-1]:
                mp[dmn[-2] + "."+dmn[-1]]+=int(num)
            mp[dmn[-1]]+=int(num)
        ans = []
        
        for j in mp:
            ans.append(str(mp[j])+" " + j)
        return ans
        