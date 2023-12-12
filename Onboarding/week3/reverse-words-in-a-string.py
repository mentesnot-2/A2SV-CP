class Solution:
    def reverseWords(self, s: str) -> str:
        listofstring=s.split()
        listofstring.reverse()
        return " ".join(listofstring)