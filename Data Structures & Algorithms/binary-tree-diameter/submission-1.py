# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(cur):
            if not cur:
                return 0
            else:
                l = dfs(cur.left)
                r = dfs(cur.right)
                nonlocal max_diameter
                max_diameter = max(max_diameter, l + r)
                return max(l, r) + 1
        
        dfs(root)
        return max_diameter