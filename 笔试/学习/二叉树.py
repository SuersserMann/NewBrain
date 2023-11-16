class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree():
    def __init__(self):
        self.root = None

    def insert(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        else:
            q = [self.root]
            while q:
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                    else:
                        cur.right = node
                        break
                else:
                    cur.left = node
                    break

    def travel(self):
        if self.root is None:
            return
        else:
            q = [self.root]
            while q:
                cur = q.pop(0)
                print(cur.item, end=' ')
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        print()

    def forward(self, root):
        if not root:
            return
        print(root.item, end=' ')
        self.forward(root.left)
        self.forward(root.right)

    def middle(self, root):
        if not root:
            return

        self.middle(root.left)
        print(root.item, end=' ')
        self.middle(root.right)

    def back(self, root):
        if not root:
            return
        self.back(root.left)
        self.back(root.right)
        print(root.item, end=' ')


tree = Tree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.travel()
tree.forward(tree.root)
