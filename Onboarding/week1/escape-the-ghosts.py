class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        ghostSteps = min(abs(x - target[0]) + abs(y - target[1]) for x, y in ghosts)
        return abs(target[0]) + abs(target[1]) < ghostSteps