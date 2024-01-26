class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitNumber = defaultdict(int)
        left = 0
        maxFruits = 0
        for i in range(len(fruits)):
            fruitNumber[fruits[i]]+=1
            while len(fruitNumber) > 2:
                fruitNumber[fruits[left]]-=1
                if fruitNumber[fruits[left]] == 0:
                    del fruitNumber[fruits[left]]
                left+=1
            
            maxFruits = max(maxFruits,i - left + 1)
        return maxFruits
        