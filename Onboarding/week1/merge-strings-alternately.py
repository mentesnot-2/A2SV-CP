class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=len(word1)
        n=len(word2)
        k=min(m,n)
        j=0
        i=0
        res=""
        while j<k and i<k:
            res=res+word1[j]
            res=res+word2[i]
            j+=1
            i+=1
        if j<m:
            res=res + word1[j:m]
        if i<n:
            res=res+word2[i:n]
        return res
            