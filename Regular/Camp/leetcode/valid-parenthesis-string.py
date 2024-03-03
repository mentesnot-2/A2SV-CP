class Solution:
    def checkValidString(self, s: str) -> bool:
        mn,mx = 0, 0

        for bra in s:
            if bra == "(":
                mn+=1
                mx+=1
            elif bra == "*":
                mn-=1
                mx+=1
            elif bra == ")":
                mn-=1
                mx-=1
            if mn < 0:
                mn = 0
            if mx < 0:
                return False
        if mn  == 0:
            return True
        else:
            return False

        