class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        consecutive = defaultdict()
        # l = 0
        mn = float("inf")
        for i in range(len(cards)):
            if cards[i] in consecutive:
                mn = min(mn,i - consecutive[cards[i]] + 1)
                del consecutive[cards[i]]
            consecutive[cards[i]] = i
            print(i)
        return mn if mn != float("inf") else -1
        