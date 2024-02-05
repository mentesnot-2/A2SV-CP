class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = set()

        for i in s:
            if i in letters:
                return i
            letters.add(i)