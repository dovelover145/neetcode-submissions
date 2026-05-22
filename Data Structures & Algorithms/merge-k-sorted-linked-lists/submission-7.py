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
    
    def mergeLists(self, list1, list2):
        dummy = cur  = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next



