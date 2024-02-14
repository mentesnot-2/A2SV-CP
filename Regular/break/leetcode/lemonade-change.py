class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                five+=1
            elif bills[i] == 10:
                ten+=1
                if five == 0:
                    return False
                else:
                    five-=1
            elif bills[i] == 20:
                
                if ten == 0 and five < 3:
                    return False
                elif 10 >= 1  and five == 0:
                    return False
                if ten >= 1:
                    ten-=1
                    five-=1
                elif ten == 0:
                    five-=3
                
                
        return True