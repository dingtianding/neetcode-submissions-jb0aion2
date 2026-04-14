#[30,38,30,36,35,40,28]
#[(38,1),(36,3),(35,4)] (40,5)
#[1,0,0,0,0,0,0]
#
#

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI


            stack.append((t, i))
        
        return res