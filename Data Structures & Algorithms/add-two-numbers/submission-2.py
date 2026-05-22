# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l3 = ListNode(0, None)
        carry = 0
        while l1 and l2:
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
            l3.next = ListNode(carry, None)
        
        return head.next
