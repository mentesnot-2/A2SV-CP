class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s:
            if i.isalpha():
                ans+=i.lower()
            elif i.isdigit():
                ans+=i
        left,right = 0,len(ans) -1
        
        while left < right:
            if ans[left] != ans[right]:
                return False
            left+=1
            right-=1
        return True
        