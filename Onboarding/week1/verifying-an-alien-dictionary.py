class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        mp = {c:i for i,c in enumerate(order)}
        mc = [[mp[c] for c in w] for w in words]
        return not any(x > y for (x,y) in zip(mc,mc[1:]))
        