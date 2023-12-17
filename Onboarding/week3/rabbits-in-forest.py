class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mp = {}
        n = len(answers)
        for i in range(n):
            mp[answers[i]] = mp.get(answers[i],0) + 1

        cnt = 0

        for j in mp:
            if mp[j] <= j + 1:
                cnt+=(j + 1)
            else:
                val = mp[j]
                while val > j + 1:
                    cnt+=(j + 1)
                    val-=(j + 1)
                if val != 0:
                    cnt+=(j + 1)
        return cnt


        