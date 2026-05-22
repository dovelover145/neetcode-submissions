# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst_aux(node, cur_min, cur_max):
            if not node:
                return True
            else:
                if cur_min < node.val < cur_max:
                    return is_valid_bst_aux(node.left, cur_min, node.val) and is_valid_bst_aux(node.right, node.val, cur_max)
                else:
                    return False
        return is_valid_bst_aux(root, float('-inf'), float('inf'))