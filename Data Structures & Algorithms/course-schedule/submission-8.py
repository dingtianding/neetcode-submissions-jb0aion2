class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AdjList = {i:[] for i in range(numCourses)}
        #{0:[1,]}
        for crs, pre in prerequisites:
            AdjList[crs].append(pre)

        visited = set()

        def dfs(course):#loking through adjulist logic
            if course in visited:
                return False #cycle detect
            if AdjList[course] == []: #can start-> everything we look up to this point can be finished
                return True
            visited.add(course)
            for pre in AdjList[course]: ##{0:[1,]}
                if not dfs(pre):#can finish
                    return False
            visited.remove(course)
            AdjList[course] = []#can finish
            return True
                
        for n in range(numCourses):
            if not dfs(n): #can't finish
                return False

        return True
        