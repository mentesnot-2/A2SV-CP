class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        mp = defaultdict(int)

        for i in range(len(edges)):
            mp[edges[i]]+=i
           

        mx = max(mp.values())
        ky = []

        for key in mp:
            if mp[key] > mx:
                mx = mp[key]
                ky.append(key)
            elif mp[key] == mx:
                ky.append(key)
        ky.sort()
        
        return ky[0]
            
