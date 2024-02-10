class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = [0] * len(customers)
        sum = 0
        ans = len(customers)
        penalty = len(customers)

        for i in range(len(customers)):
            if customers[i] == "Y":
                prefix[i] += 1
            if i > 0:
                prefix[i] += prefix[i - 1]
        prefix = [0] + prefix
        print(prefix)

        for i in range(len(customers) + 1):
            pnlty = i - prefix[i] + prefix[-1] - prefix[i]
            if pnlty < penalty:
                ans = i
                penalty = pnlty

        return ans


