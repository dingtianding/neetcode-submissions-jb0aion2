class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

        
    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


    def _insert(self, node):
        prev = self.right.prev #old most recent
        nxt = self.right

        node.prev = prev
        node.next = nxt

        prev.next = node
        nxt.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
    
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next #node to the next of left dummy
            self._remove(lru)
            del self.cache[lru.key]

        
