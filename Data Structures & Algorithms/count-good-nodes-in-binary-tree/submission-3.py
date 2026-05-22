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
                res = 0
                if node.val >= cur_max:
                    res += 1
                    cur_max = node.val
                res += good_nodes_aux(node.left, cur_max)
                res += good_nodes_aux(node.right, cur_max)
                return res
            else:
                return 0
        return good_nodes_aux(root, root.val)