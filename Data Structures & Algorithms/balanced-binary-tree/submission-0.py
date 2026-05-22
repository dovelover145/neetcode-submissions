# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            else:
                v1, h1 = dfs(root.left)
                v2, h2 = dfs(root.right)
                if not v1 or not v2:
                    return [False, max(h1, h2) + 1]
                else:
                    if abs(h1 - h2) <= 1:
                        return [True, max(h1, h2) + 1]
                    else:
                        return [False, max(h1, h2) + 1]
        
        return dfs(root)[0]
