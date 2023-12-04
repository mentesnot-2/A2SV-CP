class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        val=candies[0]
        for i in range(1,len(candies)):
            if candies[i]>val:
                val=candies[i]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=val:
                candies[i]=True
            else:
                candies[i]=False
        return candies
        