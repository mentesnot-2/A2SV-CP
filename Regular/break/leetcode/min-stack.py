class MinStack:

    def __init__(self):
        self.stack=[]
        self.MinStack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.MinStack:
            res = min(val,self.MinStack[-1])
            self.MinStack.append(res)
        else:
            self.MinStack.append(val)
        # res=min(val,self.MinStack[-1] if self.MinStack else val)
        # self.MinStack.append(res)
    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.MinStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()