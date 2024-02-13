class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        pref = [0]
        timeM,timeG,timeP = 0,0,0
        n = len(garbage)
        timeTot = defaultdict(int)
        for i in range(len(travel)):
            pref.append(pref[-1] + travel[i])

        freq = defaultdict(int)
        for k in range(len(garbage)):
            val = Counter(garbage[k])
            for key in val:
                freq[key]+=val[key]
        visited = set()
        for i in range(n -1, -1,-1):
            val = Counter(garbage[i])
            for key in val:
                if key in visited:
                    continue
                else:
                    timeTot[key]+=(freq[key] + pref[i])
                visited.add(key)
        return sum(timeTot.values())


        