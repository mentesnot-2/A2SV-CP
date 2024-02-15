class BrowserHistory:

    def __init__(self, homepage: str):
       self.store=[]
       self.visit(homepage)
    def visit(self, url: str) -> None:
        self.store.append(url)
        self.future=[]
    def back(self, steps: int) -> str:
        while len(self.store)>1 and steps>0:
            self.future.append(self.store.pop())
            steps-=1
        return self.store[-1]
    def forward(self, steps: int) -> str:
        while self.future and steps>0:
            self.store.append(self.future.pop())
            steps-=1
        return self.store[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)