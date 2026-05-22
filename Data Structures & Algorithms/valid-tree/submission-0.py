class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency_list = defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v) 
            adjacency_list[v].append(u)
        
        visited = set()

        def dfs(u, prev):
            if u in visited:
                return False
            
            visited.add(u)
            
            for v in adjacency_list[u]:
                if v == prev:
                    continue
                if not dfs(v, u):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visited)
        