class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque([i for i,c in enumerate(senate) if c == "R"])
        dire = deque([j for j,c in enumerate(senate) if c == "D"])

        while radiant and dire:
            if radiant[0] < dire[0]:
                dire.popleft()
                radiant.append(radiant.popleft() + n)
            else:
                radiant.popleft()
                dire.append(dire.popleft() + n)
        return "Radiant" if radiant else "Dire"
