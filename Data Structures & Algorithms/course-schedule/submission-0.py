class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = defaultdict(list)
        for course, prerequisite in prerequisites:
            prerequisiteMap[course].append(prerequisite)
        
        currentPath = set()
        
        def dfs(course):
            if course in currentPath:
                return False
            
            currentPath.add(course)
            
            for prerequisite in prerequisiteMap[course]:
                if not dfs(prerequisite):
                    return False
            
            currentPath.remove(course)
            prerequisiteMap[course] = []
            
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        