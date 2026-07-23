class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create pairs of car's position and speed
        #sort by starting position
        #create a stack
        #go through each pair.
        pair = [(p, s) for p, s in zip(position, speed)]

        pair.sort(reverse = True)
        stack = []

        for p, s in pair:
            time = (target - p)/ s
            stack.append(time)
            if len(stack)>= 2 and stack[-1] <= stack[-2]:#more recent takes less time
                stack.pop() #combine/keep one

        return len(stack)

