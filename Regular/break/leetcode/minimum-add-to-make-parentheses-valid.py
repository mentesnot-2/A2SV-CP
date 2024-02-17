class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opn,close = 0,0

        for i in s:
            if i == "(":
                opn+=1
            else:
                if opn == 0:
                    close+=1
                else:
                    opn-=1
        return opn + close