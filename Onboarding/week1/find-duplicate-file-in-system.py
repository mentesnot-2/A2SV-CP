class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        mp,ans = defaultdict(list),[]

        for path in paths:
            sep = path.split(" ")

            for i in range(1,len(sep)):
                part = sep[i].split("(")
                content = part[1][:-1]
                mp[content].append(sep[0] + "/" + part[0])
        for j in mp.values():
            if len(j) > 1: ans.append(j)
        return ans
        