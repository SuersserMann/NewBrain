class Node():
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


list = [3, 6, 4, 7, 9, 10, 2, 1]


class Tree:
    def __init__(self):
        self.root = None

    def insert_rank(self):
        if list:
            for i in range(len(list)):
                if i == 0:
                    node = Node(list[0])
                    self.root = node

                else:
                    cur = self.root
                    while cur:
                        if list[i] > cur.item:
                            if cur.right:
                                cur = cur.right
                            else:
                                new=Node(list[i])
                                cur.right = new
                                break
                        if list[i] < cur.item:
                            if cur.left:
                                cur = cur.left
                            else:
                                new = Node(list[i])
                                cur.left = new
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

    def middle(self, root):
        if not root:
            return

        self.middle(root.left)
        print(root.item, end=' ')
        self.middle(root.right)


tree = Tree()
tree.insert_rank()
tree.travel()
tree.middle(tree.root)
