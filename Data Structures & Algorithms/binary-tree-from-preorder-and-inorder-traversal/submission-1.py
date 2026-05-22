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
        cur_val = preorder[0]
        cur_node = TreeNode(cur_val)
        i = inorder.index(cur_val)
        inorder_l, inorder_r = inorder[:i], inorder[i + 1:]
        preorder_l, preorder_r = preorder[1:len(inorder_l) + 1], preorder[len(inorder_l) + 1:]
        cur_node.left, cur_node.right = self.buildTree(preorder_l, inorder_l), self.buildTree(preorder_r, inorder_r)
        return cur_node