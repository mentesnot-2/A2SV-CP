class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        mn = count = blocks[:k].count('W')
        for i in range(k,len(blocks)):
            count = count - (blocks[i - k] == 'W') + (blocks[i] == 'W')
            mn = min(mn, count)
        return mn
        