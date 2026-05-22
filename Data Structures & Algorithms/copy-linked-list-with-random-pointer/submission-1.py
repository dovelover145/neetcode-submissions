"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur_orig, cur_new = head, None
        head_new = cur_new
        i = 0
        dict = {}
        
        while cur_orig:
            new = Node(cur_orig.val, None, None)
            if cur_new == None:
                cur_new = new
                head_new = cur_new
            else:
                cur_new.next = new
                cur_new = cur_new.next
            dict[cur_orig] = new
            cur_orig = cur_orig.next
            i += 1
        
        cur_new = head_new
        cur_orig = head
        while cur_orig:
            cur_new.random = dict.get(cur_orig.random, None)
            cur_new = cur_new.next
            cur_orig = cur_orig.next
        
        return head_new
