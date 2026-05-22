# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr = fast_ptr = head

        while fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
            
            if fast_ptr == None:
                return False
            
            fast_ptr = fast_ptr.next

            if slow_ptr is fast_ptr:
                return True

        return False