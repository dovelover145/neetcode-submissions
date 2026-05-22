# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good_nodes_aux(node, cur_max):
            if node:
                res = 1 if node.val >= cur_max else 0
                res += good_nodes_aux(node.left, max(cur_max, node.val))
                res += good_nodes_aux(node.right, max(cur_max, node.val))
                return res
            else:
                return 0
        return good_nodes_aux(root, root.val)