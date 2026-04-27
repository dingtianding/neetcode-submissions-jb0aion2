class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #Input: tasks = [[1,4],[3,3],[2,1]]
        #Output: [0,2,1]
        #first value = when it is avalaule to proces
        #2nd value = processing time
        # return the order processing
        # CPU idle is no task
        # CPU pick the shrotest processing time.
        for i, t in enumerate(tasks):
            t.append(i) # tag orginal index pos to each tasks
        tasks.sort(key=lambda t:t[0]) #sort based on eariliest availab.e

        res, minHeap = [],[]#minheap is the ready to work tasks first pos is the lowest processing time
        i = 0
        time = tasks[0][0] #start time at the first tasks

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:#if in range and time exceed current task's ready time
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])#put the procesisngtime+index pos into minheap
                i += 1#move onto next 

            if not minHeap:#if no tasks ready
                time = tasks[i][0] #move to the next avalaible tasks
            else:
                procTime, index = heapq.heappop(minHeap)#get a task from heap
                time += procTime #update time to the after it process
                res.append(index) #add that index to res.
        return res
        
        