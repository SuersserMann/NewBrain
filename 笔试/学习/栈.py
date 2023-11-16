#先进后出
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return len(self.items) - 1

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.peek)
print(s.isEmpty())
print(s.size())
