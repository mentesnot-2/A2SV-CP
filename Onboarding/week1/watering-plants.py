class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        final = [0] + plants
        step = 0
        val = capacity
        for i in range(1,len(final)):
           
            if final[i] > val:
                step+=(2 * i - 1)
                val = capacity
                
            elif final[i] <= val:
                step+=1
            val-=final[i]
            
            
        return step
        