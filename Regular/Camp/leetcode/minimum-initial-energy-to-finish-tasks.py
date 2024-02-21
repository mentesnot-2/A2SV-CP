class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        energy = 0
        min_energy = 0
        tasks.sort(key = lambda x:x[0] - x[1])

        for x,y in tasks:
            if energy < y:
                min_energy+=(y - energy)
                energy = y - x
            else:
                energy-=(x)
        return min_energy