from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        queue = deque([(n, 0)])
        while queue:
            cur_n, cur_steps = queue.popleft()
            if cur_n**0.5 == int(cur_n**0.5):
                return cur_steps+1
            for i in range(1, int(cur_n**0.5)+1):
                queue.append((cur_n-i*i, cur_steps+1))