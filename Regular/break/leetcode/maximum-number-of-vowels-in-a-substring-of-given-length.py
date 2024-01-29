class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=['a', 'e', 'i', 'o','u']
        count=0
        val=0
        l=0
        for i in range(k):
            if s[i] in vowel:
                count+=1
        print(count)
        val=max(val,count)
        for i in range(k,len(s)):
            if s[l] in vowel:
                count-=1
            if s[i] in vowel:
                count+=1
            val=max(count,val)
            l+=1
        return val
