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

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        #node's prev and next to variables
        #point prev's next pointer to next
        #pointer next's prev pointer to prev

    def insert(self, node):
        next = self.right
        prev = self.right.prev
        node.prev = prev
        node.next = next
        next.prev = node
        prev.next = node

        #use the right dummy
        #set right and the right most node to variable
        #set right most's next to new node
        #set right dummary's prev to new node



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        #check if it exist
        #remove from cache
        #add to the end
        #return the val of that
        #if not exist, return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        #check if it exist
        #remove from cache
        #create a new one
        #add to end

        #if greater than cap
        #eject via left dummyhead
        #left.next is already oldest
        #remove lru + del it from cache

        
