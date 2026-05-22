# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kth_smallest_aux(node, cur_k):
            if not node:
                return [0, cur_k] # 0 is a dummy value that doesn't matter here
            res, cur_k = kth_smallest_aux(node.left, cur_k)
            if not cur_k:
                return [res, cur_k]
            cur_k -= 1
            if not cur_k:
                return [node.val, cur_k]
            return kth_smallest_aux(node.right, cur_k)
        return kth_smallest_aux(root, k)[0]