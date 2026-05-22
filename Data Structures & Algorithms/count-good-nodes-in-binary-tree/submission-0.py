# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def good_nodes_aux(node, cur_max):
            if node:
                if node.val >= cur_max:
                    nonlocal res
                    res += 1
                good_nodes_aux(node.left, max(cur_max, node.val))
                good_nodes_aux(node.right, max(cur_max, node.val))
        good_nodes_aux(root, root.val)
        return res