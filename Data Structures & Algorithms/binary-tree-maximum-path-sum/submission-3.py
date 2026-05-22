# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def max_path_sum_aux(node):
            nonlocal res
            if not node:
                return 0
            l, r = max_path_sum_aux(node.left), max_path_sum_aux(node.right)
            res = max(res, l + node.val + r, l + node.val, node.val, node.val + r)
            return node.val + max(l, r, 0)
        max_path_sum_aux(root)
        return res