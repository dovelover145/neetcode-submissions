# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def levelOrderAux(root, res, level):
            if root:
                if len(res) < level:
                    res.append([])
                res[level - 1].append(root.val)
                levelOrderAux(root.left, res, level + 1)
                levelOrderAux(root.right, res, level + 1)
        res = []
        levelOrderAux(root, res, 1)
        return res