class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find_parent(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(node_1, node_2):
            parent_1, parent_2 = find_parent(node_1), find_parent(node_2)
            
            if parent_1 == parent_2:
                return False
            
            if rank[parent_1] > rank[parent_2]:
                parent[parent_2] = parent_1
                rank[parent_1] += rank[parent_2]
            else:
                parent[parent_1] = parent_2
                rank[parent_2] += rank[parent_1]
            
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
            