class Solution:
    def isValid(self, s: str) -> bool: 
        pair = {"}":"{","]":"[",")":"("}
        stack = []

        for i in s:
            if stack and i == "}" :
                if stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            elif stack and  i == "]" :
                if stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif stack and  i == ")" :
                if stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return False if stack else True