class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for i in tokens:
            if i=="*":
                res2=stack.pop()
                res1=stack.pop()
                stack.append(res1*res2)
            elif i=="/":
                res2=stack.pop()
                res1=stack.pop()
                stack.append(int(res1/res2))
            elif i=="+":
                res2=stack.pop()
                res1=stack.pop()
                stack.append(res1+res2)
            elif i=="-":
                res2=stack.pop()
                res1=stack.pop()
                stack.append(res1-res2)
            else:
                stack.append(int(i))
        return stack[0]