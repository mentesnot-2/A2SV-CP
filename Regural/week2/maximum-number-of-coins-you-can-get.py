class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coins = 0
        n = len(piles)
        piles.sort(reverse = True)
        i = 1
        j = n - 1
        while i < j:
            coins+=piles[i]
            i+=2
            j-=1
            
        return coins
        