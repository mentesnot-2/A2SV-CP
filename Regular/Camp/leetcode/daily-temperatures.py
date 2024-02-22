class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        i = 0
        while i < n:
            while stack and temperatures[stack[-1]] < temperatures[i]:
                indx = stack.pop()
                ans[indx] = i - indx
            stack.append(i)
            i+=1
        return ans
