class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        odd = 0
        ans = 0
        for val in counter.values():
            if val % 2 == 0: ans+=val
            else:
                odd = 1
                ans+=(val - 1)
        return ans + odd