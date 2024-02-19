class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        i,j = 0,len(palindrome) - 1
        pal = list(palindrome)
        if len(palindrome) == 1:
            return ""
        while i < j:
            if pal[i] == pal[j] != "a":
                pal[i] = "a"
                break
            i+=1
            j-=1
        if "".join(pal) == palindrome:
            
            pal[-1]  = "b"

        return "".join(pal)       