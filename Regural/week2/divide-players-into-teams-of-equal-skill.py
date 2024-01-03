class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        l,r = 0,len(skill) - 1
        ans = skill[l] + skill[r]
        while l < r:
            if skill[l] + skill[r] != ans:
                return -1
            l+=1
            r-=1
        chemistry = 0
        l,r = 0,len(skill) - 1
        while l < r:
            chemistry+=(skill[l] * skill[r])
            r-=1
            l+=1
        return chemistry

        