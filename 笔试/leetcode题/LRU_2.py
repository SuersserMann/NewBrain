class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.stack = []

    def get(self, key: int) -> int:
        if key in self.dict:
            self.stack.remove(key)
            self.stack.append(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        n = len(self.dict)
        if key in self.dict:
            self.dict[key] = value
            self.stack.remove(key)
            self.stack.append(key)
        else:
            if n >= self.capacity:
                del self.dict[self.stack.pop(0)]
                self.dict[key] = value
                self.stack.append(key)
            else:
                self.dict[key] = value
                self.stack.append(key)