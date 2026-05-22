class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find_parent(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]] # Path compression to improve efficiency
                res = parent[res]
            return res
        
        def union(node_1, node_2):
            parent_1, parent_2 = find_parent(node_1), find_parent(node_2)
            
            if parent_1 == parent_2:
                return 0
            
            if rank[parent_1] > rank[parent_2]:
                parent[parent_2] = parent_1
                rank[parent_1] += rank[parent_2]
            else:
                parent[parent_1] = parent_2
                rank[parent_2] += rank[parent_1]
            
            return 1
        
        count = n
        for u, v in edges:
            count -= union(u, v)
        
        return count
