#[30,38,30,36,35,40,28]
#[(38,1),(36,3),(35,4)] (40,5)
#[1,0,0,0,0,0,0]
#
#

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #create a stack and result(set as zero)
        stack = []
        res = [0] * len(temperatures)

        #go through each temp while keep track of i
        #add cur temp + index to stack
        #if cur temp is higher than top of the stack, you pop top of the stack out
        # you get temp and index, you use the index to update the result array
        # next = current index - popped index.
        #keep on doing it
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                diff = i - index
                res[index] = diff

            stack.append((t, i))

        return res
        #return res
