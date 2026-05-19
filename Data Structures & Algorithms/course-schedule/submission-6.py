class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(c):
            if c in visiting:
                return False
            if preMap[c] == []:
                return True
            visiting.add(c)
            for pre in preMap[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            preMap[crs] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True