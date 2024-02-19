class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                val = 0
                while stack and stack[-1] != 0:
                    val += stack.pop()
                stack.pop() 
                stack.append(1 if val == 0 else 2 * val)
        
        return sum(stack)
