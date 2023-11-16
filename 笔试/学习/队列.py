# 先进先出
class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

list=['a','b','c','d','e','f']

q = Queue()
for i in list:
    q.enqueue(i)
while q.size()>1:
    for i in range(6):
        kid=q.dequeue()
        q.enqueue(kid)
    q.dequeue()
print(q.dequeue())