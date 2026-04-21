class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:# no height no good
            return 0 
        
        l, r = 0, len(height) - 1 #set pointeres
        leftMax, rightMax = height[l], height[r] #start max on left and r pointer
        res = 0

        while l < r: #loop
            if leftMax < rightMax: #if left is worse
                l += 1 #move left to improve
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else: #if right is worse
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        