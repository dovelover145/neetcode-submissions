# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def level_order_aux(node, level):
            if node:
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                level_order_aux(node.left, level + 1)
                level_order_aux(node.right, level + 1)
        level_order_aux(root, 0)
        return res