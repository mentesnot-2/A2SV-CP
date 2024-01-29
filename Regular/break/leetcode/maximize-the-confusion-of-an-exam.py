class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        dct = {"T":0,"F":0}
        s = answerKey
        l = 0
        ans = 0
        for i in range(len(answerKey)):
            dct[s[i]]+=1
            while dct["F"] > k and dct["T"] > k:
                dct[s[l]]-=1
                l+=1
            ans = max(ans,i - l + 1)
        return ans