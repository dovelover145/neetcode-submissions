# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        head, list1_node, list2_node = None, list1, list2
        if list1_node.val <= list2_node.val:
            head = list1_node
            list1_node = list1_node.next
        else:
            head = list2_node
            list2_node = list2_node.next
        
        prev = head

        while list1_node and list2_node:
            if list1_node.val <= list2_node.val:
                prev.next = list1_node
                prev = list1_node
                list1_node = list1_node.next
            else:
                prev.next = list2_node
                prev = list2_node
                list2_node = list2_node.next
        
        prev.next = list1_node if list1_node else list2_node
        
        return head