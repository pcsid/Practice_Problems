from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        totalWater = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]  # Update leftMax if current height is higher
                else:
                    totalWater += leftMax - height[left]  # Water trapped is leftMax - current height
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]  # Update rightMax if current height is higher
                else:
                    totalWater += rightMax - height[right]  # Water trapped is rightMax - current height
                right -= 1

        return totalWater
