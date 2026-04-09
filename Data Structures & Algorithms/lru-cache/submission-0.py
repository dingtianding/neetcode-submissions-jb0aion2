class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: #if already exist.
            self.cache.move_to_end(key) #move to end
        self.cache[key] = value #set that

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False) #eject the first one
        
