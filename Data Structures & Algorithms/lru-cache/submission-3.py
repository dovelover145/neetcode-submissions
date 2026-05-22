class ListNode:

    def __init__(self, key=0, value=0, forward=None, backward=None):
        self.key = key
        self.value = value
        self.forward = forward
        self.backward = backward

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.dummy = ListNode(key=0, value=0, forward=None, backward=None)
        self.dummy.forward = self.dummy.backward = self.dummy
    
    def get(self, key: int) -> int:
        selected = self.dict.get(key, ListNode(value=-1))
        if selected.value == -1:
            return -1
        selected.backward.forward = selected.forward
        selected.forward.backward = selected.backward
        selected.backward = self.dummy
        selected.forward = self.dummy.forward
        self.dummy.forward.backward = selected
        self.dummy.forward = selected
        return selected.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            to_update = self.dict[key]
            to_update.value = value
            to_update.backward.forward = to_update.forward
            to_update.forward.backward = to_update.backward
            to_update.backward = self.dummy
            to_update.forward = self.dummy.forward
            self.dummy.forward.backward = to_update
            self.dummy.forward = to_update
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