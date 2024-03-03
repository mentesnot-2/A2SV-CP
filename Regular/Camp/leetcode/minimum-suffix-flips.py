class Solution:
    def minFlips(self, target: str) -> int:
        target = list(target)
        if "1" not in target:
            return 0
        indx = target.index("1")
        ans = 0
        one = True
        while indx <  len(target):
            ans+=1
            if one:
                while indx < len(target) and target[indx] == "1":
                    indx+=1
                one = False
            elif not one:
                while indx < len(target) and  target[indx] == "0":
                    indx+=1
                one = True
        return ans


        
        return 3
