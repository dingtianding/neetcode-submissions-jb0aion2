class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.right.prev = self.left
        self.left.next = self.right

    def _remove(self, node):
        prev = node.prev #access prev node from the input
        nxt = node.next #access next node from the input
        prev.next = nxt #updatae prev node's pointer
        nxt.prev = prev #update nxt node's pointer

    def _insert(self, node):
        prev = self.right.prev # prev of the insertion point
        nxt = self.right #next of the insertion point
        prev.next = node #pointer to node
        nxt.prev = node #pointer to node
        node.next = nxt #pointer from node
        node.prev = prev #pointer from node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
        
