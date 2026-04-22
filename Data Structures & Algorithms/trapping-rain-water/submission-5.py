class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        l,r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if height[l] < height[r]: #move l
                l += 1
                leftMax = max(leftMax, height[l])#last peak
                res += leftMax - height[l] #if start going down since peak, we capture the area
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res