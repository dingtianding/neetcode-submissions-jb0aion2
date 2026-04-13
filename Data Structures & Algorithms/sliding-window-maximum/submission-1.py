class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = r = 0
        #Input: nums = [1,2,1,0,4,2,6], k = 3

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:#if q have stuff, and last pos is less than next number
                q.pop()
            q.append(r)#q = [1] l = 0, r = 1

            if l > q[0]: # 0 = 1 eject any that is out of window.
                q.popleft() 
            
            if (r + 1) >= k: #if at window size
                output.append(nums[q[0]]) #add the 0 pos number(largest)
                l += 1 #moves left
            r += 1 #move right

        return output
        