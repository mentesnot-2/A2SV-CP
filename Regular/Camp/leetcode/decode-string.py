class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i=="]":
                curr=""
                while stack and not stack[-1].isdigit():
                    if stack[-1]=="[":
                        stack.pop()
                        break
                    curr=stack.pop()+curr
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                if num=="":
                    num=1
                stack.append(curr*int(num))
                curr=""
                num=""
            else:
                stack.append(i)
        return "".join(stack)