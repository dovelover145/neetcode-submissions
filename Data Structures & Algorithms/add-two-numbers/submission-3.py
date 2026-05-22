# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = l3 = ListNode(0, None)
        carry = 0
        
        ''' while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            l3.next = ListNode(sum % 10, None)
            l1, l2, l3 = l1.next, l2.next, l3.next
        
        while l1:
            sum = l1.val + carry
            carry = sum // 10
            l3.next = ListNode(sum % 10, None)
            l1, l3 = l1.next, l3.next
        
        while l2:
            sum = l2.val + carry
            carry = sum // 10
            l3.next = ListNode(sum % 10, None)
            l2, l3 = l2.next, l3.next
        
        if carry:
            l3.next = ListNode(carry, None) '''
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            carry = sum // 10
            l3.next = ListNode(sum % 10, None)
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            l3 = l3.next

        return dummy.next
