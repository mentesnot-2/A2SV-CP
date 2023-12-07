class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        los = {}
        for winner,loser in matches:
            win[winner] = win.get(winner,0) + 1
            los[loser] = los.get(loser,0) + 1

        winner = []

        for i in win:
            if i not in los or los[i] == 0:
                winner.append(i)

        losser = []
        for j in los:
            if los[j] == 1:
                losser.append(j)
        winner.sort()
        losser.sort()
        return [winner,losser]