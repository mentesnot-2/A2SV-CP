class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trappedWater,curr = 0,0
        stack = []

        while curr < n:
            while stack and height[stack[-1]] < height[curr]:
                top_tower = stack.pop()
                if not stack:
                    break
                region_length = curr - stack[-1] - 1
                region_height = min(height[curr],height[stack[-1]]) - height[top_tower]
                trappedWater = trappedWater + region_length * region_height
            stack.append(curr)
            curr+=1
        return trappedWater
                