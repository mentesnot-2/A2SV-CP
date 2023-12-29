class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        n = len(s)
        ans = [0] * n

        for i in range(n):
            curr_word = s[i]
            curr_index = int(curr_word[-1])
            curr_val = curr_word[:-1]
            ans[curr_index - 1] = curr_val
        return " ".join(ans)
        