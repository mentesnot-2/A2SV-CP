class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0

        for indx,ticket in enumerate(tickets):
            if indx <= k:
                ans+=min(ticket,tickets[k])
            else:
                ans+=min(ticket,tickets[k] - 1)
        return ans