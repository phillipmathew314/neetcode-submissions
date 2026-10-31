class Node:
    def __init__(self, key: int, val: int, next: Node=None, prev: Node=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.lru_head = Node(key=0,val=0)
        self.lru_tail = Node(key=0,val=0)
        self.lru_head.next = self.lru_tail
        self.lru_tail.prev = self.lru_head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            temp_prev = node.prev
            temp_next = node.next
            temp_prev.next = temp_next
            temp_next.prev = temp_prev

            head_next = self.lru_head.next
            node.next = head_next
            node.prev = self.lru_head
            self.lru_head.next = node
            head_next.prev = node

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.cache:
            node = self.cache[key]
            temp_prev = node.prev
            temp_next = node.next
            temp_prev.next = temp_next
            temp_next.prev = temp_prev

            node.val = value
        else:
            if self.size < self.capacity:
                self.size += 1
            else:
                tail = self.lru_tail.prev
                self.cache.pop(tail.key)
                tail.prev.next = self.lru_tail
                self.lru_tail.prev = tail.prev

        node = Node(key=key, val=value)
        self.cache[key] = node

        head_next = self.lru_head.next
        node.next = head_next
        node.prev = self.lru_head
        self.lru_head.next = node
        head_next.prev = node
        
