class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # spaces = set(spaces)
        n = len(s)
        for i in range(len(spaces)):
            s =s[:spaces[i] + i ] + " " + s[spaces[i] + i:]
        return s