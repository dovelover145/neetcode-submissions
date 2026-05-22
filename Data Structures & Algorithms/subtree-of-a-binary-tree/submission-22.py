# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.is_equal(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def is_equal(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif root and subRoot and root.val == subRoot.val:
            return self.is_equal(root.left, subRoot.left) and self.is_equal(root.right, subRoot.right)
        else:
            return False