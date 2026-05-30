class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses #an array to track which course is ready to be taken
        #index = respective course
        adj = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            indegree[pre] += 1
            adj[course].append(pre)

        q = deque()#init the que
        for n in range(numCourses):
            if indegree[n] == 0:#okay to taken
                q.append(n)
                
        finish = 0
        output = []

        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in adj[node]:#check all the adj 
                indegree[nei] -= 1#reduce those course's indegree by one since one was taken
                if indegree[nei] == 0: #if its ready to take
                    q.append(nei) #add it to our q

        if finish != numCourses:
            return []

        return output[::-1]
