# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(cur: ListNode, k: int) -> Optional[ListNode]:
            while cur and k > 0:
                cur = cur.next
                k -= 1
            return cur
        
        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            kth = getKth(prev_group, k)
            if not kth:
                break
            
            group_next = kth.next
            
            prev, cur = kth.next, prev_group.next # Not None
            while cur != group_next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
        
        return dummy.next