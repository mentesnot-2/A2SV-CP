class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j] == s[j:i:-1]:
                    palindromes += 1
        return palindromes