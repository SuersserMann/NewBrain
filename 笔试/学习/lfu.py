class ListNode():
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.count = {}
        self.min_count = 1
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def movehead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        # 一定要注意一个问题，就是记住修改顺序

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.movehead(self.hashmap[key])

            return self.hashmap[key].val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.movehead(self.hashmap[key])
            self.hashmap[key].val = value
            return
        else:
            new = ListNode(key, value)
            if len(self.hashmap) == self.capacity:
                del self.hashmap[self.tail.prev.key]
                self.movehead(new)
                self.remove(self.tail.prev)
                self.hashmap[key] = new

            else:
                self.movehead(new)
                self.hashmap[key] = new
