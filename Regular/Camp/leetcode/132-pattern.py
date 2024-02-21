class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        if n < 3:return False
        minimum = [0] * n
        minimum[0] = nums[0]
        for i in range(1,n):
            minimum[i] = min(minimum[i - 1],nums[i])
        for i in range(n - 1, -1,-1):
            currNum = nums[i]
            currMin = minimum[i]
            if currNum > currMin:
                while stack and stack[-1] <= currMin:
                    stack.pop()
                if stack and stack[-1] < currNum:
                    return True
            stack.append(currNum)
        return False