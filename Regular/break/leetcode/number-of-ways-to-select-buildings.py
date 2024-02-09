class Solution:
    def numberOfWays(self, s: str) -> int:
        _mp = Counter(s)
        val = int(s[0])
        count0 = 0
        count1 = 0
        ans = 0
        if val == 0:
            count0 = 1
        elif val == 1:
            count1 = 1
        for i in range(1,len(s) - 1):
            if s[i] == "0":
                count0+=1
                r_one = _mp["1"] - count1
                if r_one == 0 or _mp["1"] == r_one:
                    continue
                else:
                    ans+=(r_one * count1)
            else:
                count1+=1
                r_zero = _mp["0"] - count0
                if r_zero == _mp["0"]:
                    continue
                ans+=(r_zero * count0)
        return ans

