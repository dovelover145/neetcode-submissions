# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def max_path_sum_aux(root):
            nonlocal res
            if not root:
                return 0
            l, r = max_path_sum_aux(root.left), max_path_sum_aux(root.right)
            l, r = max(l, 0), max(r, 0)
            res = max(res, l + root.val + r)
            return root.val + max(l, r)
        max_path_sum_aux(root)
        return res