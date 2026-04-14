class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre) #use crs as index to look up pre

        visiting = set()
        visited = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited: #avoid loop
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            visited.add(crs)

            return True



        for c in range(numCourses):
            if not dfs(c):
                return False

        return True