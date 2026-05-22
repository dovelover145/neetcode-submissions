# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kth_smallest_aux(node, count):
            if not node:
                return [0, count]
            val1, new_count1 = kth_smallest_aux(node.left, count)
            if new_count1 == k:
                return [val1, new_count1]
            new_count1 += 1
            if new_count1 == k:
                return [node.val, new_count1]
            return kth_smallest_aux(node.right, new_count1)
        count = 0
        return kth_smallest_aux(root, count)[0]