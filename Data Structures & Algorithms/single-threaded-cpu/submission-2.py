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
            t.append(i)
        tasks.sort(key=lambda t:t[0])

        res, minHeap = [],[]
        i = 0
        time = tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not minHeap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
        return res
        
        