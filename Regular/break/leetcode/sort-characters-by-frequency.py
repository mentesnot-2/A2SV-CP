class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(list(s))
        output=[]
        for char in sorted(freq,key=lambda x:freq[x],reverse=True):
            output.append(char*freq[char])
        return "".join(output)
        