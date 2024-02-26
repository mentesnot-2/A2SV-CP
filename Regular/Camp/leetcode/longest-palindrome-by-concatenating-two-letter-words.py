class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dct = {}
        sum_ = 0
        cc_odd_ind = 0


        for word in words:
            dct[word] = dct.get(word,0) + 1
        for key,val in dct.items():
            if key[0] == key[1]:
                sum_+=val//2 * 2
                if val % 2 == 1:
                    cc_odd_ind = 1
            else:
                sum_+=min(dct.get(key,0),dct.get(key[::-1],0))
        return (sum_ + cc_odd_ind) * 2
