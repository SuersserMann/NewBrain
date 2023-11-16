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
        #一定要注意一个问题，就是记住修改顺序

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


# 创建一个容量为3的LRU缓存
cache = LRUCache(3)

# 添加数据
cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)

# 查询数据
print(cache.get(1))  # 输出: 10
print(cache.get(2))  # 输出: 20
print(cache.get(4))  # 输出: -1 (键4不在缓存中)

# 添加更多数据，容量已满，会移除最近未使用的数据
cache.put(4, 40)

# 查询数据
print(cache.get(3))  # 输出: -1 (键3已经被移除)
print(cache.get(4))  # 输出: 40

# 添加新数据，容量已满，会移除最近未使用的数据
cache.put(5, 50)

# 查询数据
print(cache.get(1))  # 输出: -1 (键1已经被移除)
print(cache.get(5))  # 输出: 50
