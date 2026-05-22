# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        head, list1_node, list2_node = None, list1, list2
        if list1.val < list2.val:
            head = list1
            list1_node = list1_node.next
        else:
            head = list2
            list2_node = list2_node.next
        prev = head

        while True:
            if list1_node == None:
                prev.next = list2_node
                break
            elif list2_node == None:
                prev.next = list1_node
                break
            if list1_node.val < list2_node.val:
                prev.next = list1_node
                prev = list1_node
                list1_node = list1_node.next
            else:
                prev.next = list2_node
                prev = list2_node
                list2_node = list2_node.next
        
        return head