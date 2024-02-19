class RecentCounter:

    def __init__(self):
        self.recentCall = deque()
    def ping(self, t: int) -> int:
        self.recentCall.append(t)
        numberOfCalls = 0
        while self.recentCall and self.recentCall[0] < self.recentCall[-1] - 3000 :
            self.recentCall.popleft()
            
        return len(self.recentCall)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)