# I am using a circular doubly linked list with a dummy node
class ListNode:

    def __init__(self, key=0, value=0, forward=None, backward=None):
        self.key, self.value, self.forward, self.backward = key, value, forward, backward

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.dummy = ListNode(key=0, value=0, forward=None, backward=None)
        self.dummy.forward = self.dummy.backward = self.dummy # You can reference yourself
    
    def __move(self, to_move: ListNode, prev: ListNode) -> None:
        to_move.backward.forward = to_move.forward
        to_move.forward.backward = to_move.backward
        to_move.backward = prev
        to_move.forward = prev.forward
        prev.forward.backward = to_move
        prev.forward = to_move

    def get(self, key: int) -> int:
        to_get = self.dict.get(key, ListNode(key=-1, value=-1, forward=None, backward=None))
        if to_get.key == to_get.value == -1:
            return to_get.key
        self.__move(to_get, self.dummy)
        return to_get.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            to_update = self.dict[key]
            to_update.value = value
            self.__move(to_update, self.dummy)
            return
        
        if len(self.dict) == self.capacity:
            to_evict = self.dummy.backward
            self.dummy.backward = to_evict.backward
            to_evict.backward.forward = self.dummy
            to_evict.forward = to_evict.backward = None
            _ = self.dict.pop(to_evict.key)
        
        to_add = ListNode(key=key, value=value, forward=self.dummy.forward, backward=self.dummy)
        self.dummy.forward.backward = to_add
        self.dummy.forward = to_add
        self.dict[key] = to_add