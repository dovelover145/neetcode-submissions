# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ''' if not len(lists):
            return None
        
        dummy = ListNode(0, lists[0]) # Add a dummy node for simpler code (fire rhyme)
        lists[0] = dummy
        
        for i in range(1, len(lists)):
            prev_list, cur_list = lists[i - 1], lists[i]
            while cur_list:
                if prev_list.next and prev_list.next.val <= cur_list.val:
                    prev_list = prev_list.next
                else:
                    temp = cur_list.next
                    cur_list.next = prev_list.next
                    prev_list.next = cur_list
                    prev_list = cur_list
                    cur_list = temp     
            lists[i] = lists[i - 1]
        
        return lists[-1].next '''

        if not len(lists):
            return None
        
        for i in range(1, len(lists)):
            lists[i] = self.mergeLists(lists[i - 1], lists[i])
        
        return lists[-1]
    
    def mergeLists(self, l1: List[ListNode], l2: List[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        
        return dummy.next