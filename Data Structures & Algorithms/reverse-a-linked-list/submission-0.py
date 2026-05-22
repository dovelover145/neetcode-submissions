# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head # None or a node
        new_node = None
        while cur_node != None:
            next_node = cur_node.next
            cur_node.next = new_node
            new_node = cur_node
            cur_node = next_node
        return new_node