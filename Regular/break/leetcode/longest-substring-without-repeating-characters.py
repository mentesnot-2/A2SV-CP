class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        unique = {}
        longest = 0
        for i in range(len(s)):
            if s[i] in unique:
                if left <= unique[s[i]]:
                    left = unique[s[i]] + 1
                
            unique[s[i]] = i
            
            longest = max(longest,i - left + 1)
            
        return longest
        