class ListNode():
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])
            self.move_head(self.dict[key])
            return self.dict[key].val
        else:
            return -1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def put(self, key: int, value: int) -> None:
        n = len(self.dict)
        if key in self.dict:
            self.remove(self.dict[key])
            self.move_head(self.dict[key])
            self.dict[key].val = value

        else:
            new = ListNode(key, value)
            if n >= self.capacity:
                self.dict.pop(self.tail.prev.key)
                self.remove(self.tail.prev)
                self.move_head(new)
                self.dict[key] = new
            else:
                self.move_head(new)
                self.dict[key] = new


s = LRUCache(2)
s.put(1, 1)
s.put(2, 2)
s.get(1)
s.put(3, 3)
s.get(2)
s.put(4, 4)
s.get(1)
s.get(3)
s.get(4)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
