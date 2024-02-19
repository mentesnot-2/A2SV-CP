class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left,right = [None] * n,[None] * n,
        s1,s2 = [],[]

        for i in range(n):
            cnt = 1

            while len(s1) > 0 and s1[-1][0] > arr[i]:
                cnt+=(s1[-1][1])
                s1.pop()
            s1.append([arr[i],cnt])
            left[i] = cnt
        for i in range(n - 1, - 1, -1):
            cnt = 1

            while len(s2) > 0 and s2[-1][0] >= arr[i]:
                cnt+=(s2[-1][1])
                s2.pop()
            s2.append([arr[i],cnt])
            right[i] = cnt
        ans = 0

        for i in range(n):
            ans +=(arr[i] * left[i] * right[i])
        return ans %(10**9 + 7)
