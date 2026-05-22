class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisiteMap = defaultdict(list)
        for course, prerequisite in prerequisites:
            prerequisiteMap[course].append(prerequisite)
        
        res = []
        currentPath, visited = set(), set()

        def dfs(course):
            if course in currentPath:
                return False
            if course in visited:
                return True
            
            currentPath.add(course)

            for prerequisite in prerequisiteMap[course]:
                if not dfs(prerequisite):
                    return False
            
            currentPath.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
