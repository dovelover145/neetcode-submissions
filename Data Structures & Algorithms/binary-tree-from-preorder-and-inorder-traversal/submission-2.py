# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        cur_node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        cur_node.left, cur_node.right = self.buildTree(preorder[1:mid + 1], inorder[:mid]), self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return cur_node