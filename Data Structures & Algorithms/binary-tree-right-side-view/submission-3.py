# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def right_side_view_aux(node, level):
            if node:
                if len(res) == level:
                    res.append(node.val)
                right_side_view_aux(node.right, level + 1)
                right_side_view_aux(node.left, level + 1)
        right_side_view_aux(root, 0)
        return res